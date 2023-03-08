from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from http import request
import flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


# initiate login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model
class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.username
    


# User database
users = {
    'user1': User('user1', 'password1'),
    'user2': User('user2', 'password2')
}


# User loader function
@login_manager.user_loader
def load_user(username):
    return users.get(username)


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

# Logout page
@app.route('/logout')
@login_required
def logout():
    def logout():
        logout_user()
        return redirect(url_for('index'))

# Protected page
@app.route('/')
@login_required
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()