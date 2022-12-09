import 'dart:convert';

import 'package:application/api.dart' as api;

void main(List<String> arguments) async {
  Map data = await api.getRefreshToken('https://kpi.eu.auth0.com/oadsth/token');
  print(data['refresh_token']);
}
