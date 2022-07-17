from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from repositories import gym_repository
from repositories import member_repository
from repositories import session_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)