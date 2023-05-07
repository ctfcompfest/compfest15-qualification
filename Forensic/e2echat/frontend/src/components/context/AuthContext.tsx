import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import { Message } from "../types";
import { WebsocketContext } from "./WebsocketContext";
import { ProviderProps } from "./ProviderProps";

interface AuthData {
  isLoggedIn: boolean;
  username: string;
  logIn: (username: string, password: string) => void;
}

export const AuthContext = createContext<AuthData>({} as AuthData);

export const AuthContextProvider: React.FC<ProviderProps> = ({ children }) => {
  const { sendMessage, addListener } = useContext(WebsocketContext);
  const [username, setUsername] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const identListener = useCallback((message: Message) => {
    if (message.type != "server") return;
    if (message.action != "auth") return;
    if (message.message == "Authenticated") setIsLoggedIn(true);
  }, []);

  useEffect(() => {
    addListener(identListener);
  }, []);

  const logIn = (username: string, password: string) => {
    sendMessage({
      type: "ident",
      data: {
        username,
        password,
      },
    });
    setUsername(username);
  };

  return (
    <AuthContext.Provider value={{ username, isLoggedIn, logIn }}>
      {children}
    </AuthContext.Provider>
  );
};
