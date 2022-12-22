const jwt = require("jsonwebtoken");
const { config } = require("../config");
const { getUserData, refreshToken } = require("./api");

const generateAccessToken = (data) => {
  return jwt.sign(data, config.secret, { expiresIn: config.expiresIn });
};

const VerifyAccessToken = async (token) => {
  try {
    const data = await getUserData(
      "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImppYzdtZHZweTFKMEZrZlA0d1ZQXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzkyZjRkZGU0ZTJjMWFmM2ZkMTMyNzEiLCJhdWQiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjcxNzI1NjYwLCJleHAiOjE2NzE4MTIwNjAsImF6cCI6IkM0ZEZUbUh3S1Y4RFhhWGtCb0NYNFJMQW9FTkJzc3RaIiwic2NvcGUiOiJyZWFkOmN1cnJlbnRfdXNlciB1cGRhdGU6Y3VycmVudF91c2VyX21ldGFkYXRhIGRlbGV0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgY3JlYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSBjcmVhdGU6Y3VycmVudF91c2VyX2RldmljZV9jcmVkZW50aWFscyBkZWxldGU6Y3VycmVudF91c2VyX2RldmljZV9jcmVkZW50aWFscyB1cGRhdGU6Y3VycmVudF91c2VyX2lkZW50aXRpZXMgb2ZmbGluZV9hY2Nlc3MiLCJndHkiOiJwYXNzd29yZCJ9.OkS4w3obSroBlqFKDuyZhuSliqAd9ufrz50TaSc-fYxI0WUvyVLgp5PICP4PKKZDGNQRI_fg7IkOZ3Sc5ic_Ul52HN3LNqcfr_UUdjZN0vY0vvdxNpExB39Txxe1EcNbtnQnArgXQBS7fMdwiCErjl5nT0NOCiDauClRrAmFlM-4vvWobjHiATJOSNXOuYIeKZQme-rZCjVT4-uIev4-ZR9DcS0qfhK929dRDBYdrNl7YInjG56GppHFCEtfyM5byZfF5JMkmBkE1ZDWPI9w20jiFPItzYuiihYzUW6hLgBmWfEPPQXtjOKPu-N_ODOvvuXS2hPhGJJxMZ9cscXVFQ",
      "auth0|6392f4dde4e2c1af3fd13271"
    );
    console.log(data["name"]);
    return jwt.verify(token, config.secret);
  } catch (e) {
    return null;
  }
};

module.exports = {
  generateAccessToken,
  VerifyAccessToken,
};
