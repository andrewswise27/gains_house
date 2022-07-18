from db.run_sql import run_sql

from models.booked_session import BookedSession
from models.member import Member
from models.session import Session

from repositories import session_repository
from repositories import member_repository

def book_session(booking):
    sql = "INSERT INTO booked_sessions (member_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member_id, booking.session_id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    