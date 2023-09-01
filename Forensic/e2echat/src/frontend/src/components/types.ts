export interface TargetedMsg {
  fromUsername: string;
  targetUsername: string;
}

export interface IdentMsg {
  username: string;
  password: string;
}

export interface MessageMsg extends TargetedMsg {
  message: string;
  id: string;
}

export interface AckMsg extends TargetedMsg {
  id: string;
}

export interface InitMsg extends TargetedMsg {
  type: "v";
  value: string;
}

export type Message =
  | {
      type: "ident";
      data: IdentMsg;
    }
  | {
      type: "message";
      data: MessageMsg;
    }
  | {
      type: "ack";
      data: AckMsg;
    }
  | {
      type: "init";
      data: InitMsg;
    }
  | {
      type: "server";
      action: "auth" | "message";
      message: string;
    };

export interface ChatCredential {
  p: bigint;
  n: bigint | null;
  q: bigint | null;
}
