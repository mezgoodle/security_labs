const winston = require("winston");

const logger = winston.createLogger({
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
});

module.exports = {
  logger,
};
