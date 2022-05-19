from flask import render_template,request,redirect,url_for,abort

from app.main.forms import ReviewForm, UpdateProfile
from . import main
from ..request import *
from flask_login import login_required,current_user
from ..models import *
@main.route('/')
def index(): 
   title="Homepage"
   
   return render_template('index.html',title=title)

@main.route('/discover')
def discover():
   title='Discover'

   return render_template('discover.html',title=title)

@main.route('/charts/tracks')
def charts():
    allCharts = getChartTracks()

    return render_template('charts.html',charts=allCharts)

@main.route('/charts/albums')
def albums():
    allAlbums = getChartAlbums()

    return render_template('albums.html',albums=allAlbums)

@main.route('/charts/podcasts')
def podcasts():
    allPodcasts = getChartPodcasts()

    return render_template('podcasts.html',artists=allPodcasts)

@main.route('/charts/artists')
def artists():
    allArtists = getChartArtists()

    return render_template('artists.html',artists=allArtists)

@main.route('/contact')
def contact():

    return render_template('contact.html')

@main.route('/discover/album/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    album = getChartAlbums(id)#assumed there is a model class album with properties including id,cover_medium from the api,also assumed there is a method called get_album in requests.py
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(album_id=album.id,album_title=title,image_path=album.cover_medium,album_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.album',id = album.id ))#assumed there is a view (main.album) to display a single album and it's properties

    title = f'{album.title} review'
    return render_template('new_review.html',title = title, review_form=form, album=album)

 
@main.route('/upvote/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    albums = Upvote.query_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for album in albums:
        to_str = f'{album}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.album',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, album_id = album.id)
    new_vote.save_Upvote()
    return redirect(url_for('main.albums',id=id))#view for all the albums
 
 
@main.route('/downvote/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    albums = Downvote.query_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for album in albums:
        to_str = f'{album}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.album',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, album_id= album.id)
    new_downvote.save_downvote()
    return redirect(url_for('main.albums',id = id))


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.update_profile',uname=user.username))

    return render_template('profile/update.html',form =form)

