import 'package:application/api.dart' as api;
import 'package:application/config.dart';

void main(List<String> arguments) async {
  print('Getting refresh token from the KPI application');
  Map refreshTokenData = await api.getRefreshToken(config['KPI']['URL'],
      config['KPI']['USERNAME'], config['KPI']['PASSWORD']);
  String refreshToken = refreshTokenData['refresh_token'];
  String firstToken = refreshTokenData['access_token'];
  print('Refresh token is: $refreshToken');
  Map tokenData = await api.refreshToken(
      'https://kpi.eu.auth0.com/oauth/token', refreshToken);
  String secondToken = tokenData['access_token'];
  print('Are the access tokens are similiar - ${firstToken == secondToken}');
}
