import React, { useContext, useEffect, useState } from "react";
import { ChatContext } from "../../context/ChatContext";
import { decryptMessage, expmod, modInverse } from "../../../utils/rsa";
import { ChatCredential, MessageMsg } from "../../types";
import { AuthContext } from "../../context/AuthContext";

interface ChatListProps {
  currentChat: string;
  credential: ChatCredential;
  messages: MessageMsg[];
}

const ChatList: React.FC<ChatListProps> = ({
  currentChat,
  credential,
  messages,
}) => {
  const { username } = useContext(AuthContext);

  if (!currentChat) {
    return <p>No chat selected</p>;
  }

  if (credential.q == null || credential.n == null) {
    return <p>Still exchanging keys</p>;
  }

  const totient = (credential.p - 1n) * (credential.q - 1n);
  const privKey = modInverse(0x10001n, totient);

  return (
    <>
      {messages.map((message) => (
        <div
          className={
            "chat " +
            (message.fromUsername == username ? "chat-end" : "chat-start")
          }
          key={message.id + "-" + message.fromUsername}
        >
          <div className="chat-bubble">
            {decryptMessage(BigInt(message.message), privKey, credential.n!)}
          </div>
        </div>
      ))}
    </>
  );
};

const MemoizedChatList = React.memo(ChatList);

const ChatArea = () => {
  const { currentChat, chats, sendChat, credentials } = useContext(ChatContext);
  const [message, setMessage] = useState("");

  useEffect(() => setMessage(""), [currentChat]);

  return (
    <div className="h-full flex flex-col">
      <div className="p-4 font-bold text-white bg-slate-600">
        {currentChat == "" ? "No chat selected" : currentChat}
      </div>

      <div className="flex flex-col grow overflow-y-auto px-4 py-2">
        <MemoizedChatList
          currentChat={currentChat}
          credential={credentials[currentChat]}
          messages={chats[currentChat]}
        />
      </div>

      <div className="flex flex-row gap-2 p-4 justify-stretch">
        <input
          type="text"
          placeholder="Type here"
          className="input input-bordered w-full"
          disabled={currentChat == ""}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button
          className="btn btn-primary"
          disabled={currentChat == ""}
          onClick={() => {
            sendChat(currentChat, message);
            setMessage("");
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatArea;
