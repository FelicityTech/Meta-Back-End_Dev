# Require authentication to access sensitive data
from flask_login import login_required

#Only allow authenticated users to view their own data
@login_required
def view_profile():
    user_id = current_user.get_id()
    user_data = db.execute('SELECT * FROM users WHERE id = ?', (user_id)).fetchone()
    return render_template('profile.html', user_data=user_data)

