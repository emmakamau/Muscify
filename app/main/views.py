from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import Review
from .forms import ReviewForm

@main.route('/')
def index(): 
   title="Homepage"
   
   return render_template('index.html',title=title)

@main.route('/discover')
def discover():
   title='Discover'

   return render_template('discover.html',title=title)

@main.route('/discover/album/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    album = get_album(id)#assumed there is a model class album with properties including id,cover_medium from the api,also assumed there is a method called get_album in requests.py
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(album_id=album.id,album_title=title,image_path=album.cover_medium,album_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.album',id = album.id ))

    title = f'{album.title} review'
    return render_template('new_review.html',title = title, review_form=form, album=album)