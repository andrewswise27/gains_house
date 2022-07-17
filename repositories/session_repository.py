from sqlite3 import SQLITE_ALTER_TABLE
from db.run_sql import run_sql

from models.gym import Gym
from models.member import Member
from models.session import Session

from repositories import member_repository
from repositories import gym_repository

def save(session):
    sql = "INSERT INTO sessions (name, tod, doy, length, capacity, level, description) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ID"
    values = [session.name, session.tod, session.doy, session.length, session.capacity, session.level, session.description]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for row in results:
        session = Session(row['name'], row['tod'], row['doy'], row['length'], row['capacity'], row['description'], row['level'], row['id'])
        sessions.append(session)
    return sessions

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def select_session(id):
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    session = Session(results['name'], results['tod'], results['doy'], results['length'], results['capacity'], results['description'], results['level'], results['id'])
    return session
