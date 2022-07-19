from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
from repositories import booked_session_repository
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
    members = booked_session_repository.booked_members(session)
    return render_template("sessions/description.html", session=session, members=members)

@sessions_blueprint.route("/home/session", methods=['POST'])
def create_session():
    print(request.form)
    name = request.form['session_name']
    timedate = request.form['timedate']
    length = request.form['length']
    capacity = request.form['capacity']
    description = request.form['description']
    level = request.form['level']
    
    
    session = Session(name, timedate, length, capacity, description, level)

    session_repository.save(session)
    return redirect('/sessions')

@sessions_blueprint.route("/sessions/edit/<id>")
def edit_view(id):
    session = session_repository.select_session(id)
    return render_template("/sessions/edit.html", session=session)

@sessions_blueprint.route("/sessions/edit/<id>", methods=['POST'])
def edit(id):
    name = request.form['session_name']
    timedate = request.form['timedate']
    length = request.form['length']
    capacity = request.form['capacity']
    description = request.form['description']
    level = request.form['level']

    session = session_repository.select_session(id)
    session.name = name
    session.timedate = timedate
    session.length = length
    session.capacity = capacity
    session.description = description
    session.level = level

    session_repository.edit(session)

    return redirect("/sessions")

@sessions_blueprint.route('/sessions/delete/<id>', methods=['POST'])
def delete_session(id):
    session_repository.delete(id)
    return redirect('/sessions')
