import React, { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";

const LoginModal = () => {
  const { isLoggedIn, logIn } = useContext(AuthContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div className={"modal " + (isLoggedIn ? "" : "modal-open")}>
      <div className="modal-box flex flex-col gap-4">
        <h3 className="font-bold text-lg">Log in</h3>
        <input
          type="text"
          placeholder="Username"
          className="input input-bordered w-full"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          className="input input-bordered w-full"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="btn" onClick={() => logIn(username, password)}>
          Log In
        </button>
      </div>
    </div>
  );
};

export default LoginModal;
