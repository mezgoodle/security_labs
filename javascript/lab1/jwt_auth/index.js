const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const port = 3000;
const jwt_utils = require("./jwt");
const { config } = require("../config");

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const users = [
  {
    login: "Login",
    password: "Password",
    username: "Username",
  },
  {
    login: "Login1",
    password: "Password1",
    username: "Username1",
  },
];

const verifyUser = (token) => {
  const data = jwt_utils.VerifyAccessToken(token);
  if (!data) {
    return null;
  }
  const user = users.find((user) => user.login == data.login);
  if (!user) {
    return null;
  }
  return user.username;
};

app.use((req, res, next) => {
  const sessionId = req.get(config.session_key);

  req.username = verifyUser(sessionId);
  req.sessionId = sessionId;

  next();
});

app.get("/", (req, res) => {
  if (req.username) {
    return res.json({
      username: req.username,
      logout: "http://localhost:3000/logout",
    });
  }
  res.sendFile(path.join(__dirname + "/index.html"));
});

app.get("/logout", (req, res) => {
  res.redirect("/");
});

app.post("/api/login", (req, res) => {
  const { login, password } = req.body;

  const user = users.find(
    (user) => user.login == login && user.password == password
  );

  if (user) {
    const token = jwt_utils.generateAccessToken({ login: user.login });
    console.log(token);
    res.json({ token });
  }

  res.status(401).send();
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
