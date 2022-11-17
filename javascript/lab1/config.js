const winston = require("winston");

const config = {
  secret:
    "82b2b2b3c1cc0dd8443d9b3b7ec2b4088f28f9bcf9dcb84e55feb98e10f77e78561d2c1465429cd295aeb4082a0c3379471169b4a344d0d0acf4363f576e04ee",
  expiresIn: "1800s",
  session_key: "Authorization",
  logger: winston.createLogger({
    level: "info",
    format: winston.format.combine(
      winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
      winston.format.json()
    ),
    defaultMeta: { service: "user-service" },
    transports: [
      new winston.transports.File({ filename: "error.json", level: "error" }),
      new winston.transports.File({ filename: "combined.json", level: "info" }),
    ],
  }),
};

module.exports = {
  config,
};
