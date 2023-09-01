import { ChatContextProvider } from "../context/ChatContext";
import LoginModal from "./LoginModal";
import ChatArea from "./chat/ChatArea";
import Sidebar from "./chat/Sidebar";

const ChatApp = () => {
  return (
    <div>
      <LoginModal />
      <ChatContextProvider>
        <div className="flex flex-row w-full">
          <Sidebar />

          <div className="h-screen w-full">
            <ChatArea />
          </div>
        </div>
      </ChatContextProvider>
    </div>
  );
};

export default ChatApp;
