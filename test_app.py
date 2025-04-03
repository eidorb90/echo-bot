"""
test_echo.py
Ian Kollipara <ian.kollipara@cune.edu>
2025-03-04

Testing Echo Bot
"""

from unittest import TestCase

from app import app


class testEchoBot(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_echo__post__pass(self):
        response = self.client.post("/echo", json={"text": "my text"})

        self.assertEqual(response.content_type, "application/json")
        self.assertIn("text", response.json)
        self.assertEqual("MY  TEXT", response.json["text"])

    def test_echo__post__fail__invalid_type(self):
        response = self.client.post("/echo", data=b"my text")
        self.assertEqual(response.content_type, "application/json")
        self.assertNotIn("text", response.json)
        self.assertIn("error", response.json)
        self.assertEqual(415, response.status_code)

    def test_echo__post__fail__invalid_json(self):
        response = self.client.post(
            "/echo", data=b'{"text": my text"}', content_type="application/json"
        )

        self.assertEqual(response.content_type, "application/json")
        self.assertNotIn("text", response.json)
        self.assertIn("error", response.json)
        self.assertEqual(422, response.status_code)

    def test_echo__post__fail__invalid_json_data(self):
        response = self.client.post("/echo", json={"data": "my text"})

        self.assertEqual(response.content_type, "application/json")
        self.assertNotIn("text", response.json)
        self.assertIn("error", response.json)
        self.assertEqual(422, response.status_code)
