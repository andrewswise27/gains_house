from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
from repositories import gym_repository
from repositories import member_repository
from repositories import session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("/sessions/index.html", sessions=sessions)

@sessions_blueprint.route("/session/description/<id>")
def description(id):
    session = session_repository.select_session(id)
    return render_template("sessions/description.html", session=session)

@sessions_blueprint.route("/home", methods=['POST'])
def create_session():
    name = request.form['session_name']
    tod = request.form['tod']
    doy = request.form['doy']
    length = request.form['length']
    capacity = request.form['capacity']
    description = request.form['description']
    level = request.form['level']
    
    session = Session(name, tod, doy, length, capacity, description, level)

    session_repository.save(session)
    return redirect('/sessions')
