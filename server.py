"""
Jeremy Krovitz

This file creates routes for the home page where all reviews are listed. It also
creates routes for the pages where a movie review is created, edited, viewed, and
deleted.
"""

from database import Database, reviewFactory
from flask import Flask, render_template, flash, request, url_for, redirect
from my_form import ReviewForm

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_pyfile('server.cfg')
db = Database(app)

"""
Use the following commands to interact with the database:
db.get() to get all of the reviews
db.get(id) to get a single review
db.create(title, text, rating) to add a new review
db.update(id, title, text, rating) to update a review
db.delete(id) to delete a review
"""

#This route is the home page where users get a list of reviews.
@app.route('/')
@app.route('/home')
def home():
    reviews = db.get()
    return render_template('home.html', reviews=reviews)

""" A route is defined to create a review. The function
creates a new review and if the form is successfully
validated on submit, the user is redirected to the
home page. """
@app.route('/review/new', methods=['GET', 'POST'])
def new_review():
    form = ReviewForm()
    print("before db get id")
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        rating = form.rating.data
        review = db.create(title, text, rating)
        flash('Your review has been created!', 'success')
        return redirect(url_for('home', review=review))
    return render_template('create_review.html', title='New Review',
                           form=form, legend='New Review')

#This function gets the id of an individual review.
@app.route('/review/<int:id>')
def get_review_id(id):
    review = db.get(id)
    return render_template('review.html', title=review.title, text=review.text, rating=review.rating, review=review)

""" This function allows the user to view the movie's details and allows
the user to choose to update a particular review."""
@app.route('/review/<int:id>/update', methods=['GET', 'POST'])
def update_review(id):
    review = db.get(id)
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        rating = form.rating.data
        updated_review = db.update(id, title, text, rating)
        flash('Your review has been updated!', 'success')
        return redirect(url_for('home', title=review.title, text=review.text, rating=review.rating, id=review.id))
    return render_template('create_review.html', title='Update Review', form=form, legend='Update Review')

""" This function allows the user to delete their review
by getting the review's id. The user is redirected
to the home page listing all of the reviews upon
deletion of a review with a specific id."""
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_review(id):
    db.delete(id)
    flash('Your review has been deleted!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
