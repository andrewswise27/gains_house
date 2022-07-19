from sqlite3 import SQLITE_ALTER_TABLE
from db.run_sql import run_sql

from models.booked_session import BookedSession
from models.member import Member
from models.session import Session

from repositories import member_repository
from repositories import booked_session_repository

def save(session):
    sql = "INSERT INTO sessions (name, timedate, length, capacity, level, description) VALUES (%s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [session.name, session.timedate, session.length, session.capacity, session.level, session.description]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions ORDER BY timedate"
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['timedate'], row['length'], row['capacity'], row['description'], row['level'], row['id'])
        sessions.append(session)
    return sessions

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def select_session(id):
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    session = Session(results['name'], results['timedate'], results['length'], results['capacity'], results['description'], results['level'], results['id'])
    return session

def edit(session):
    sql = "UPDATE sessions SET (name, timedate, length, capacity, description, level) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.timedate, session.length, session.capacity, session.description, session.level, session.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
