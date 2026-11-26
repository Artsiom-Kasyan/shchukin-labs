#!/usr/bin/env bash
set -eu
url=http://localhost:8000/bookings
room="demo-$(date +%s%N)"
payload=$(printf '{"room":"%s","start":"2026-10-01T09:00Z","end":"2026-10-01T10:00Z"}' "$room")
post() {
    curl -sS -o /dev/null -w '%{http_code}' -H 'Content-Type: application/json' -d "$payload" "$url"
}
test "$(post)" = 201
test "$(post)" = 409
curl -fsS "$url?day=2026-10-01" | python3 -c 'import json, sys; assert any(r["room"] == sys.argv[1] for r in json.load(sys.stdin))' "$room"
echo 'Создание, конфликт и выборка на дату прошли проверку.'
