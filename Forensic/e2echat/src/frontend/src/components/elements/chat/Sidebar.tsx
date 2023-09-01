import React, { useContext, useState } from "react";
import { ChatContext } from "../../context/ChatContext";
import { AuthContext } from "../../context/AuthContext";

const Sidebar = () => {
  const { chats, initChat, setCurrentChat } = useContext(ChatContext);
  const { username: currUsername, isLoggedIn } = useContext(AuthContext);
  const [username, setUsername] = useState("");

  return (
    <div className="h-screen bg-slate-200 basis-1/3 max-w-xs">
      <div className="p-4 font-bold text-white bg-slate-600">
        {isLoggedIn ? `Hello, ${currUsername}!` : "Unauthenticated"}
      </div>

      <div className="flex flex-col gap-4 p-2">
        <label htmlFor="my-modal-4" className="btn btn-primary w-full">
          New chat
        </label>
      </div>

      {Object.entries(chats).map(([username, messages]) => (
        <div
          className="flex flex-col gap-1 text-black hover:bg-slate-100 p-2 hover:cursor-pointer"
          key={username}
          onClick={() => setCurrentChat(username)}
        >
          <strong className="font-bold">{username}</strong>
          <p className="overflow-hidden">
            {messages.length == 0
              ? "No messages"
              : "Messages: " + messages.length}
          </p>
        </div>
      ))}

      <input type="checkbox" id="my-modal-4" className="modal-toggle" />
      <label htmlFor="my-modal-4" className="modal cursor-pointer">
        <label className="modal-box relative flex flex-col gap-4" htmlFor="">
          <h3 className="text-lg font-bold">New Chat</h3>
          <input
            type="text"
            placeholder="Username"
            className="input input-bordered w-full"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <button className="btn" onClick={() => initChat(username)}>
            Open
          </button>
        </label>
      </label>
    </div>
  );
};

export default Sidebar;
