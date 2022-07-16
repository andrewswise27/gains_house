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

# @sessions_blueprint.route("/session/description/")
# def description(id) ------- render template for individual session. show the description and people booked
