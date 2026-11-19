import requests

BASE = "http://127.0.0.1:5000/api"
tests = [
    ("add", 5, 3),      # Should succeed (200)
    ("divide", 9, 0)    # Should fail politely (400)
]

for op, a, b in tests:
    r = requests.get(f"{BASE}/{op}", params={"a": a, "b": b})
    print(op, a, b, "->", r.status_code, r.json())