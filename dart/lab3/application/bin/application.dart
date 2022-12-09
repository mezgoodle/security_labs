import 'package:application/application.dart' as application;
import 'package:http/http.dart' as http;

void main(List<String> arguments) async {
  var request =
      http.Request('POST', Uri.parse('https://kpi.eu.auth0.com/oauth/token'));
  request.bodyFields = {
    'grant_type': 'http://auth0.com/oauth/grant-type/password-realm',
    'scope': 'offline_access',
    'username': 'mezgoodle',
    'password': '1Max2Victor',
    'realm': 'Username-Password-Authentication'
  };

  http.StreamedResponse response = await request.send();

  if (response.statusCode == 200) {
    print(await response.stream.bytesToString());
  } else {
    print(response.reasonPhrase);
  }
}
