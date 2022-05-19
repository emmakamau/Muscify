from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import *
from flask_login import login_required,current_user
from ..models import *
from .forms import *

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

    return render_template('podcasts.html',podcasts=allPodcasts)

@main.route('/charts/artists')
def artists():
    allArtists = getChartArtists()

    return render_template('artists.html',artists=allArtists)


@main.route('/charts/tracks/<trackId>', methods = ['GET','POST'])
def track(trackId):
    track = getTrack(trackId)
    review_form = ReviewForm()
    reviews = Review.get_reviews(trackId)
    if review_form.validate_on_submit():
        title = review_form.title.data
        review = review_form.review.data

        # Updated review instance
        new_review = Review(track_id=track.id,image_path=track.cover_medium,track_review=review,user=current_user)
        new_review.save_review()
        return redirect('/tracks/{track_id}'.format(track_id=trackId))
    return render_template('charts-detail.html',track=track,reviews=reviews,review_form=review_form)


# @main.route('/discover/track/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#     form = ReviewForm()
#     track = getTrack(id)
#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data

#         # Updated review instance
#         new_review = Review(track_id=track.id,album_title=title,image_path=track.cover_big,track_review=review,user=current_user)

#         # save review method
#         new_review.save_review()
#         return redirect(url_for('.album',id = album.id ))

#     title = f'{album.title} review'
#     return render_template('new_review.html',title = title, review_form=form, album=album)

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


# @main.route('/charts/playlists')
# def playlists():
#     allArtists = getChartPlaylists()

#     return render_template('playlists.html',playlists=allArtists)
