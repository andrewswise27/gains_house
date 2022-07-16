from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
from repositories import gym_repository
from repositories import member_repository
from repositories import session_repository

gyms_blueprint = Blueprint("gyms", __name__)