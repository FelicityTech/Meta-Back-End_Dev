from flask import Flask, render_template, redirect, url_for
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECURITY_PASSWORD_SALT'] = 'password_salt'


# initialize security
from models import db, User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
Security = Security(app, user_datastore)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.')
        return render_template('login.html')
# logout page

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Protected page
@app.route('/')
@login_required
def index():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    admin_role = Role(name='admin')
    user_datastore.create_role(admin_role)
    admin_user = User(email='admin@example.com', password='password')
    user_datastore.add_role_to_user(admin_user, admin_role)
    db.session.add(admin_user)
    db.session.commit()
    app.run()



    # This code uses Flask-Security to set up a user database, 
    # user authentication, and user roles. The User model includes 
    # a check_password method that checks whether a given password 
    # matches the user's hashed password. The @login_required 
    # decorator is used to protect the index page and ensure that 
    # only authenticated users can access it.