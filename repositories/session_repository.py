from sqlite3 import SQLITE_ALTER_TABLE
from db.run_sql import run_sql
from datetime import datetime

from models.booked_session import BookedSession
from models.member import Member
from models.session import Session

from repositories import member_repository
from repositories import booked_session_repository

def save(session):
    sql = "INSERT INTO sessions (name, timedate, length, capacity, level, description, active_session) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [session.name, session.timedate, session.length, session.capacity, session.level, session.description, session.active_session]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions ORDER BY timedate"
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['timedate'], row['length'], row['capacity'], row['description'], row['level'], row['active_session'], row['id'])
        sessions.append(session)
    return sessions

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def select_session(id):
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    session = Session(results['name'], results['timedate'], results['length'], results['capacity'], results['description'], results['level'], results['active_session'], results['id'])
    return session

def edit(session):
    sql = "UPDATE sessions SET (name, timedate, length, capacity, description, level, active_sessions) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.timedate, session.length, session.capacity, session.description, session.level, session.active_session, session.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def get_capacity(id):
    sql = "SELECT capacity FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    return results

def get_session_time(id):
    sql = "SELECT timedate :: timestamp :: time  FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    time = (results[0][0])
    seq = int(time.strftime("%H%M%S"))
    return seq

def get_active_session(id):
    sql = "SELECT active_session FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    active = (results[0][0])
    return active
