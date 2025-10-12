#!/usr/bin/env python3
import sys
import json
from pathlib import Path


def load_request() -> dict:
    try:
        data = sys.stdin.read()
        return json.loads(data) if data else {}
    except Exception:
        return {}


def suggest_matrix(matrix):
    # TODO: replace with real call into notebook logic (moved to a .py function)
    # For MVP, echo-back example: invert booleans as a "suggestion"
    if not isinstance(matrix, list):
        return []
    out = []
    for row in matrix:
        if isinstance(row, list):
            out.append([not bool(cell) for cell in row])
        else:
            out.append([])
    return out


def main():
    req = load_request()
    matrix = req.get("matrix", [])
    suggestions = suggest_matrix(matrix)
    print(json.dumps({"suggestions": suggestions}))


if __name__ == "__main__":
    main()


