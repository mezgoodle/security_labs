import 'package:application/api.dart' as api;
import 'package:application/config.dart';

void main(List<String> arguments) async {
  print('Getting refresh token from the KPI application');
  Map refreshTokenData = await api.getRefreshToken(config['KPI']['URL'],
      config['KPI']['USERNAME'], config['KPI']['PASSWORD']);
  String refreshToken = refreshTokenData['refresh_token'];
  String firstToken = refreshTokenData['access_token'];
  print('Refresh token is: $refreshToken');
  Map tokenData = await api.refreshToken(config['KPI']['URL'], refreshToken);
  String secondToken = tokenData['access_token'];
  print('Are the access tokens are similiar - ${firstToken == secondToken}');

  print('\n');
  print('Getting refresh token from the MY application');
  refreshTokenData = await api.getRefreshToken(
      config['MYSELF']['URL'],
      config['MYSELF']['USERNAME'],
      config['MYSELF']['PASSWORD'],
      config['MYSELF']['CLIENT_ID'],
      config['MYSELF']['CLIENT_SECRET'],
      config['MYSELF']['AUDIENCE']);
  refreshToken = refreshTokenData['refresh_token'];
  firstToken = refreshTokenData['access_token'];
  print('Refresh token is: $refreshToken');
  tokenData = await api.refreshToken(
    config['MYSELF']['URL'],
    refreshToken,
    config['MYSELF']['CLIENT_ID'],
    config['MYSELF']['CLIENT_SECRET'],
  );
  secondToken = tokenData['access_token'];
  print('Are the access tokens are similiar - ${firstToken == secondToken}');

  tokenData = await api.getAccessToken(config['MYSELF']['URL']);
  String accessToken = tokenData['access_token'];
  Map newUser = await api.updateUser(
      'https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users/${config['MYSELF']['USER_ID']}',
      config['MYSELF']['PASSWORD'],
      accessToken);
  print('User has been updated at ${newUser['updated_at']}');
}
