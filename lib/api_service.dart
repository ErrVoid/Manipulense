import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'https://manipulense-backend.onrender.com';

  static const Map<String, String> headers = {
    'Content-Type': 'application/json',
  };

  // Health check endpoint
  Future<Map<String, dynamic>> healthCheck() async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/health'),
        headers: headers,
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Health check failed: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Network error during health check: $e');
    }
  }

  // Analyze chat endpoint
  Future<Map<String, dynamic>> analyze(String chat) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/analyze'),
        headers: headers,
        body: json.encode({'chat': chat}),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Analysis failed: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Network error during analysis: $e');
    }
  }

  // Predict text endpoint
  Future<Map<String, dynamic>> predict(String text) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/predict'),
        headers: headers,
        body: json.encode({'text': text}),
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Prediction failed: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Network error during prediction: $e');
    }
  }

  // Get user endpoint
  Future<Map<String, dynamic>> getUser(int id) async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/users/$id'),
        headers: headers,
      );

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('User fetch failed: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Network error during user fetch: $e');
    }
  }
}
