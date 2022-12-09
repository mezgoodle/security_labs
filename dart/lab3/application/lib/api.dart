import 'dart:convert';
import 'package:http/http.dart' as http;

Future<Map> getRefreshToken(String url) async {
  var response = await http.post(Uri.parse(url), body: {
    'grant_type': 'http://auth0.com/oauth/grant-type/password-realm',
    'scope': 'offline_access',
    'username': 'proksima.maxim1@gmail.com',
    'password': 'TheStrongPassword123',
    'realm': 'Username-Password-Authentication',
    'client_id': 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
    'client_secret':
        'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB'
  });
  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  }
  throw Exception(
      'Error: ${response.reasonPhrase}. Status: ${response.statusCode}');
}

Future<Map> refreshToken(String url, String token) async {
  var response = await http.post(Uri.parse(url), body: {
    'grant_type': 'refresh_token',
    'client_id': 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
    'client_secret':
        'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB',
    'refresh_token': token
  });
  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  }
  throw Exception(
      'Error: ${response.reasonPhrase}. Status: ${response.statusCode}');
}
