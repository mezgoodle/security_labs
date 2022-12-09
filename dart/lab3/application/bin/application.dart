import 'dart:convert';

import 'package:application/api.dart' as api;
import 'package:http/http.dart' as http;

void main(List<String> arguments) async {
  // var request =
  //     http.Request('POST', Uri.parse('https://kpi.eu.auth0.com/oauth/token'));
  // request.bodyFields = {
  //   'grant_type': 'http://auth0.com/oauth/grant-type/password-realm',
  //   'scope': 'offline_access',
  //   'username': 'proksima.maxim1@gmail.com',
  //   'password': 'TheStrongPassword123',
  //   'realm': 'Username-Password-Authentication',
  //   'client_id': 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
  //   'client_secret':
  //       'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB'
  // };

  // var response =
  //     await http.post(Uri.parse('https://kpi.eu.auth0.com/oauth/token'), body: {
  //   'grant_type': 'http://auth0.com/oauth/grant-type/password-realm',
  //   'scope': 'offline_access',
  //   'username': 'proksima.maxim1@gmail.com',
  //   'password': 'TheStrongPassword123',
  //   'realm': 'Username-Password-Authentication',
  //   'client_id': 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
  //   'client_secret':
  //       'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB'
  // });
  var data = await api.getRefreshToken('https://kpi.eu.auth0.com/oauth/token');
  print(data['refresh_token']);

  // if (response.statusCode == 200) {
  //   print(await response.stream.bytesToString());
  // } else {
  //   print(response.reasonPhrase);
  // }
}
