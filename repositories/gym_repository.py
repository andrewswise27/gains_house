from db.run_sql import run_sql

from models.gym import Gym
from models.member import Member
from models.session import Session

from repositories import session_repository
from repositories import member_repository

def save(gym):
    sql = "INSERT INTO gyms (name, location) VALUES (%s, %s) RETURNING ID"
    values = [gym.name, gym.location]
    results = run_sql(sql, values)
    gym.id = results[0]['id']
    return gym

def delete_all():
    sql = "DELETE FROM gyms"
    run_sql(sql)
    