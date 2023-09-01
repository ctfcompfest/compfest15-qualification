import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import { ChatCredential, Message, MessageMsg } from "../types";
import { WebsocketContext } from "./WebsocketContext";
import { ProviderProps } from "./ProviderProps";
import {
  bufToBigInt,
  encryptMessage,
  expmod,
  randomNBitPrime,
} from "../../utils/rsa";
import { AuthContext } from "./AuthContext";

interface ChatData {
  chats: Record<string, MessageMsg[]>;
  credentials: Record<string, ChatCredential>;

  currentChat: string;
  setCurrentChat: (target: string) => void;

  initChat: (target: string) => void;
  sendChat: (target: string, message: string) => void;
}

export const ChatContext = createContext<ChatData>({} as ChatData);

export const ChatContextProvider: React.FC<ProviderProps> = ({ children }) => {
  const { username } = useContext(AuthContext);
  const { addListener, sendMessage } = useContext(WebsocketContext);
  const [currentChat, setCurrentChat] = useState("");
  const [chats, setChats] = useState<Record<string, MessageMsg[]>>({});
  const [credentials, setCredentials] = useState<
    Record<string, ChatCredential>
  >({});

  const messageListener = useCallback((message: Message) => {
    if (message.type != "message") return;
    const source = message.data.fromUsername;

    setChats((chats) => {
      const newChats = { ...chats };
      if (source in chats) {
        newChats[source] = [...chats[source], message.data];
      } else {
        newChats[source] = [message.data];
      }
      return newChats;
    });
  }, []);

  const initListener = useCallback(
    async (message: Message) => {
      if (message.type != "init") return;
      const source = message.data.fromUsername;
      const v = BigInt(message.data.value);
      const isP = v < 2n ** 1024n;
      if (isP) {
        const p = v + 2n ** 1024n;
        const q = await randomNBitPrime(1024);
        const n = p * q;

        sendMessage({
          type: "init",
          data: {
            fromUsername: username,
            targetUsername: source,
            type: "v",
            value: n.toString(),
          },
        });

        setCredentials((credentials) => {
          const newCredentials = { ...credentials };
          newCredentials[source] = {
            p,
            q,
            n,
          };
          return newCredentials;
        });
      } else {
        setCredentials((credentials) => {
          const newCredentials = { ...credentials };
          const p = newCredentials[source].p;
          const n = BigInt(message.data.value);
          newCredentials[source] = {
            p,
            n,
            q: n / p,
          };
          return newCredentials;
        });
      }

      setChats((chats) => {
        const newChats = { ...chats };
        newChats[source] = [];
        return newChats;
      });
    },
    [username]
  );

  const initChat = async (target: string) => {
    const p = await randomNBitPrime(1024);
    const v = p - 2n ** 1024n;
    sendMessage({
      type: "init",
      data: {
        fromUsername: username,
        targetUsername: target,
        type: "v",
        value: v.toString(),
      },
    });

    setCredentials((credentials) => {
      const newCredentials = { ...credentials };
      newCredentials[target] = {
        p,
        n: null,
        q: null,
      };
      return newCredentials;
    });

    setChats((chats) => {
      const newChats = { ...chats };
      newChats[target] = [];
      return newChats;
    });
  };

  const sendChat = (target: string, message: string) => {
    const pubkey = credentials[target].n;
    if (!pubkey) return;

    let c = encryptMessage(message, pubkey);
    let msgData = {
      fromUsername: username,
      targetUsername: target,
      id: Date.now().toString(),
      message: c.toString(),
    };
    sendMessage({
      type: "message",
      data: msgData,
    });

    setChats((chats) => {
      const newChats = { ...chats };
      if (target in chats) {
        newChats[target] = [...chats[target], msgData];
      } else {
        newChats[target] = [msgData];
      }
      return newChats;
    });
  };

  useEffect(() => {
    if (username == "") return;
    addListener(messageListener);
    addListener(initListener);
  }, [username]);

  return (
    <ChatContext.Provider
      value={{
        chats,
        credentials,
        initChat,
        currentChat,
        setCurrentChat,
        sendChat,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};
