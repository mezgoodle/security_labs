const axios = require("axios").default;

const getUserData = async (token, userId) => {
  const response = await axios.get(
    `https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users/${userId}`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );
  return response.data;
};

const refreshToken = async (resfreshToken) => {
  try {
    const response = await axios.post(
      `https://dev-b34fyn1cot22je3i.us.auth0.com/oauth/token`,
      {
        grant_type: "refresh_token",
        client_id: "C4dFTmHwKV8DXaXkBoCX4RLAoENBsstZ",
        client_secret:
          "Hiuy2N4AdwU-zezmgVKhKHhf-5TINv_82RvwpESbV25ddoUZZ88pRWBXmQVCJ7GB",
        refresh_token: resfreshToken,
      }
    );
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

module.exports = {
  getUserData,
  refreshToken,
};
