from crypt import methods
from datetime import datetime
from time import time
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.session_controller import sessions
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
    sessions = session_repository.select_session(session_id)
    booking = BookedSession(member_id, session_id)
    num_booked = booked_session_repository.session_full(session_id)
    capacity = session_repository.get_capacity(session_id)
    membership_type = member_repository.get_membership_type(member_id)
    tod = session_repository.get_session_time(session_id)
    if membership_type == "Bronze" and tod >= 170000:
        return render_template('/bookings/membershiptype.html', sessions=sessions)
    elif num_booked >= capacity:
        return render_template('/bookings/error.html', sessions=sessions)
    else:
        booked_session_repository.book_session(booking)
    return redirect('/sessions')
