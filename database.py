from flask_sqlalchemy import SQLAlchemy

class Database:
	def __init__(self, app):
		db = SQLAlchemy(app)
		self.db = db
		self.model = reviewFactory(db)

	def get(self, id=None):
		if id:
			return self.model.query.get(id)
		return self.model.query.all()

	def create(self, title, text, rating):
		review = self.model(title, text, rating)
		self.db.session.add(review)
		self.db.session.commit()

	def update(self, id, title, text, rating):
		review = self.get(id)
		review.title = title
		review.text = text
		review.rating = rating
		self.db.session.commit()

	def delete(self, id):
		review = self.get(id)
		self.db.session.delete(review)
		self.db.session.commit()

def reviewFactory(db):
	class Review(db.Model):
		__tablename__ = 'reviews'
		id = db.Column('review_id', db.Integer, primary_key=True)
		title = db.Column(db.String(60))
		text = db.Column(db.String)
		rating = db.Column(db.Integer)

		def __init__(self, title, text, rating):
			self.title = title
			self.text = text
			self.rating = rating
	return Review
