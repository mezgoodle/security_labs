import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:application/config.dart';

Future<Map> getRefreshToken(String url, String username, String password,
    [String? clientId, String? clientSecret, String? audince]) async {
  var response = await http.post(Uri.parse(url), body: {
    'grant_type': 'http://auth0.com/oauth/grant-type/password-realm',
    'scope': 'offline_access',
    'username': username,
    'password': password,
    'realm': 'Username-Password-Authentication',
    'client_id': clientId ??= config['KPI']['CLIENT_ID'],
    'client_secret': clientSecret ??= config['KPI']['CLIENT_SECRET'],
    'audince': audince ??= config['KPI']['AUIDENCE']
  });

  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  }
  throw Exception(
      'Error: ${response.reasonPhrase}. Status: ${response.statusCode}');
}

Future<Map> refreshToken(String url, String token,
    [String? clientId, String? clientSecret]) async {
  var response = await http.post(Uri.parse(url), body: {
    'grant_type': 'refresh_token',
    'client_id': clientId ??= config['KPI']['CLIENT_ID'],
    'client_secret': clientSecret ??= config['KPI']['CLIENT_SECRET'],
    'refresh_token': token
  });
  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  }
  throw Exception(
      'Error: ${response.reasonPhrase}. Status: ${response.statusCode}');
}
