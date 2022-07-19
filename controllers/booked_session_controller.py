from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booked_session import BookedSession
from repositories import booked_session_repository
from repositories import member_repository
from repositories import session_repository

booked_session_blueprint = Blueprint("booked_sessions", __name__)

@booked_session_blueprint.route("/book/<id>", methods=['GET'])
def booking(id):
    members = member_repository.select_all()
    sessions = session_repository.select_session(id)
    return render_template("/bookings/index.html", members=members, sessions=sessions)

@booked_session_blueprint.route("/book/", methods=['POST'])
def book_member():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    booking = BookedSession(member_id, session_id)
    booked_session_repository.book_session(booking)
    return redirect('/sessions')
