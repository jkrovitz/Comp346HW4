print('Resetting database...')
from server import db
# Reset the database
db.db.drop_all()
# Create the tables
db.db.create_all()
print('Database reset: success!')
