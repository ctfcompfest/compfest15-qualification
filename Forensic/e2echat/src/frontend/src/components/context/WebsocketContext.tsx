import { createContext, useCallback, useEffect, useRef, useState } from "react";
import { Message } from "../types";
import { ProviderProps } from "./ProviderProps";
import toast from "react-hot-toast";

type WebsocketListener = (data: Message) => any;
interface WebsocketData {
  addListener: (fn: WebsocketListener) => void;
  connecting: boolean;
  socket: WebSocket | null;
  sendMessage: (message: Message) => void;
}

export const WebsocketContext = createContext<WebsocketData>(
  {} as WebsocketData
);

export const WebsocketContextProvider: React.FC<ProviderProps> = ({
  children,
}) => {
  const [connecting, setConnecting] = useState(true);
  const socket = useRef<WebSocket | null>(null);
  const listeners = useRef<WebsocketListener[]>([]);

  const onWebsocketMessage = (data: MessageEvent<string>) => {
    const message = JSON.parse(data.data) as Message;
    listeners.current.forEach((listener) => listener(message));

    if (message.type == "server") {
      toast(`${message.action}: ${message.message}`);
    }
  };

  const addListener = (fn: WebsocketListener) => {
    if (listeners.current.indexOf(fn) === -1)
      listeners.current = [...listeners.current, fn];
  };

  const sendMessage = (message: Message) => {
    socket.current!.send(JSON.stringify(message));
  };

  useEffect(() => {
    const conn = new WebSocket(import.meta.env.VITE_WS_URL);
    conn.addEventListener("open", () => setConnecting(false));
    conn.addEventListener("message", onWebsocketMessage);
    socket.current = conn;

    return () => {
      conn.close();
    };
  }, []);

  return (
    <WebsocketContext.Provider
      value={{ addListener, connecting, socket: socket.current, sendMessage }}
    >
      {children}
    </WebsocketContext.Provider>
  );
};
