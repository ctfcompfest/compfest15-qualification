import { WebsocketContextProvider } from "./components/context/WebsocketContext";
import { AuthContextProvider } from "./components/context/AuthContext";
import ChatApp from "./components/elements/ChatApp";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <WebsocketContextProvider>
      <AuthContextProvider>
        <Toaster />
        <ChatApp />
      </AuthContextProvider>
    </WebsocketContextProvider>
  );
}

export default App;
