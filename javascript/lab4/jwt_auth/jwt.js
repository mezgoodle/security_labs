const jwt = require("jsonwebtoken");
const { config } = require("../config");
const { getUserData, refreshToken, getToken } = require("./api");

const generateAccessToken = async (data) => {
  const tokenData = await getToken("mezgoodle@gmail.com", "1Max2Victor");
  return tokenData["access_token"];
  return jwt.sign(data, config.secret, { expiresIn: config.expiresIn });
};

const VerifyAccessToken = async (token) => {
  try {
    const data = await getUserData(token, "auth0|6392f4dde4e2c1af3fd13271");
    return data["name"];
    return jwt.verify(token, config.secret);
  } catch (e) {
    return null;
  }
};

module.exports = {
  generateAccessToken,
  VerifyAccessToken,
};
