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

def booked_members(session):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN booked_sessions ON booked_sessions.member_id = members.id WHERE booked_sessions.session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['age'], row['nationality'], row['mob_number'], row['email'])
        members.append(member)
    
    return members

def session_full(session):
    sql = "SELECT COUNT(member_id) FROM booked_sessions WHERE session_id = %s;"
    values = [session]
    results = run_sql(sql, values)
    return results
