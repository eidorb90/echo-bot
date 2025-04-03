"""
echo.py
Ian Kollipara <ian.kollipara@cune.edu>
2025-03-04

Echo Bot
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from http import HTTPStatus

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, allow_headers=["*"])


@dataclass(frozen=True)
class EchoBotPostRequest:
    text: str

    @classmethod
    def parse(cls, data: dict) -> EchoBotPostRequest | None:
        if data.get("text") and isinstance(data["text"], str):
            return cls(data["text"])


@app.post("/echo")
def echo():
    if request.content_type != "application/json":
        response = jsonify({"error": "Invalid Content Type"})
        response.status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
        return response

    try:
        json_ = json.loads(request.get_data())
    except json.JSONDecodeError:
        response = jsonify({"error": "Invalid JSON"})
        response.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        return response

    if data := EchoBotPostRequest.parse(json_):
        return jsonify(
            text=data.text.upper().replace(" ", "  "),
        )

    response = jsonify({"error": "Invalid JSON"})
    response.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    return response
