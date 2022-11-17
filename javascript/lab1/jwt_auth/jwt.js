const jwt = require("jsonwebtoken");
const { config } = require("../config");

const generateAccessToken = (data) => {
  return jwt.sign(data, config.secret, { expiresIn: config.expiresIn });
};

const VerifyAccessToken = (token) => {
  try {
    return jwt.verify(token, config.secret);
  } catch (e) {
    return null;
  }
};

module.exports = {
  generateAccessToken,
  VerifyAccessToken,
};
