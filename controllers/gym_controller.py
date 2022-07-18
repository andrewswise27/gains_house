from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
from repositories import gym_repository
from repositories import member_repository
from repositories import session_repository

gyms_blueprint = Blueprint("gyms", __name__)

@gyms_blueprint.route("/book/<id>", methods=['GET'])
def booking(id):
    members = member_repository.select_all()
    sessions = session_repository.select_session(id)
    return render_template("/bookings/index.html", members=members, sessions=sessions)

@gyms_blueprint.route("/book/", methods=['POST'])
def book_member():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    member = member_repository.select_member(member_id)
    session = session_repository.select_session(session_id)
    booking = (member, session)
    gym_repository.book_session(booking)
    return redirect('/sessions')
