from flask import Flask, render_template
from controllers.booked_session_controller import booked_session_blueprint
from controllers.session_controller import sessions_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(booked_session_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)