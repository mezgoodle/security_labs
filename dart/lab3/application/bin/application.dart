import 'package:application/api.dart' as api;

void main(List<String> arguments) async {
  Map refreshTokenData = await api.getRefreshToken(
      'https://kpi.eu.auth0.com/oauth/token',
      'proksima.maxim1@gmail.com',
      'TheStrongPassword123');
  String refreshToken = refreshTokenData['refresh_token'];
  String firstToken = refreshTokenData['access_token'];
  print('Refresh token is: $refreshToken');
  Map tokenData = await api.refreshToken(
      'https://kpi.eu.auth0.com/oauth/token', refreshToken);
  String secondToken = tokenData['access_token'];
  print('Are the tokens are similiar - ${firstToken == secondToken}');
}
