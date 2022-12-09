import 'dart:convert';
import 'package:http/http.dart' as http;

Future<Map> getRefreshToken(String url, String username, String password,
    {String clientId = 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
    String clientSecret =
        'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB'}) async {
  var response = await http.post(Uri.parse(url), body: {
    'grant_type': 'http://auth0.com/oauth/grant-type/password-realm',
    'scope': 'offline_access',
    'username': username,
    'password': password,
    'realm': 'Username-Password-Authentication',
    'client_id': clientId,
    'client_secret': clientSecret
  });

  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  }
  throw Exception(
      'Error: ${response.reasonPhrase}. Status: ${response.statusCode}');
}

Future<Map> refreshToken(String url, String token,
    {String clientId = 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
    String clientSecret =
        'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB'}) async {
  var response = await http.post(Uri.parse(url), body: {
    'grant_type': 'refresh_token',
    'client_id': clientId,
    'client_secret': clientSecret,
    'refresh_token': token
  });
  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  }
  throw Exception(
      'Error: ${response.reasonPhrase}. Status: ${response.statusCode}');
}
