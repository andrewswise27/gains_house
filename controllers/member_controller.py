from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from repositories import booked_session_repository
from repositories import member_repository
from repositories import session_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

@members_blueprint.route("/home", methods=['POST'])
def create_member():
    name = request.form['name']
    age = request.form['age']
    nationality = request.form['nationality']
    mob_number = request.form['mob_number']
    email = request.form['email']
    
    member = Member(name, age, nationality, mob_number, email)

    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route("/members/edit/<id>")
def edit_view(id):
    member = member_repository.select_member(id)
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/edit/<id>", methods=['POST'])
def edit(id):
    name = request.form['name']
    age = request.form['age']
    nationality = request.form['nationality']
    mob_number = request.form['mob_number']
    email = request.form['email']

    member = member_repository.select_member(id)
    member.name = name
    member.age = age
    member.nationality = nationality
    member.mob_number = mob_number
    member.email = email

    member_repository.edit(member)
    
    return redirect("/members")

@members_blueprint.route('/members/delete/<id>', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')
