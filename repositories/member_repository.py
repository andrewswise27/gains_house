from db.run_sql import run_sql

from models.gym import Gym
from models.member import Member
from models.session import Session

from repositories import session_repository
from repositories import gym_repository

def save(member):
    sql = "INSERT INTO members (name, age, nationality, mob_number, email) VALUES (%s, %s, %s, %s, %s) RETURNING ID"
    values = [member.name, member.age, member.nationality, member.mob_number, member.email]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['age'], row['nationality'], row['mob_number'], row['email'], row['id'])
        members.append(member)
    return members

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_member(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    member = Member(results['name'], results['age'], results['nationality'], results['mob_number'], results['email'], results['id'])
    return member

def edit(member):
    sql = "UPDATE members SET (name, age, nationality, mob_number, email) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.nationality, member.mob_number, member.email, member.id]
    run_sql(sql, values)



    