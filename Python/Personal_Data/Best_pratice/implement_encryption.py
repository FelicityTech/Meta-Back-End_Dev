# Encrypt sensitive data before storing it
import hashlib
from data_collection import email, name
# Hash the user's email address
email_hash = hashlib.sha256(email.encode()).hexdigest()

# store the hashed email address in the database
db.execute('INSERT INTO users (name, email_hash) VALUES (?, ?)', (name, email))