import os
from datetime import date, datetime, timedelta, timezone

import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Бронирование аудиторий")


class Slot(BaseModel):
    room: str = Field(min_length=1, max_length=64)
    start: datetime
    end: datetime


def connect():
    return psycopg.connect(host="db", dbname="rooms", user="rooms",
                           password=os.environ["POSTGRES_PASSWORD"])


@app.get("/health")
def health():
    with connect() as db:
        db.execute("SELECT 1 FROM bookings LIMIT 1")
    return {"status": "ok"}


@app.post("/bookings", status_code=201)
def book(slot: Slot):
    room = slot.room.strip()
    if not room or slot.start.tzinfo is None or slot.end.tzinfo is None or slot.start >= slot.end:
        raise HTTPException(422, "Укажите аудиторию и непустой интервал с часовым поясом")
    try:
        with connect() as db:
            row = db.execute(
                "INSERT INTO bookings(room, period) VALUES (%s, tstzrange(%s,%s,'[)')) RETURNING id",
                (room, slot.start, slot.end),
            ).fetchone()
    except psycopg.errors.ExclusionViolation:
        raise HTTPException(409, "Аудитория занята в это время")
    return {"id": row[0]}


@app.get("/bookings")
def list_bookings(day: date):
    start = datetime.combine(day, datetime.min.time(), tzinfo=timezone.utc)
    with connect() as db:
        rows = db.execute(
            "SELECT id, room, lower(period), upper(period) FROM bookings "
            "WHERE period && tstzrange(%s,%s,'[)') ORDER BY lower(period), id",
            (start, start + timedelta(days=1)),
        ).fetchall()
    return [dict(zip(("id", "room", "start", "end"), row)) for row in rows]
