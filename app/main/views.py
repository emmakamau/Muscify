from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import *
from flask_login import login_required,current_user
from ..models import *
from .forms import *
from .. import db, photos

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

# Display each track and add reviews
@main.route('/charts/tracks/<trackId>', methods = ['GET','POST'])
@login_required
def track(trackId):
    track = getTrack(trackId)
    review_form = ReviewForm()
    reviews = Review.get_reviews(trackId)
    if review_form.validate_on_submit():
        review = review_form.review.data

        # Updated review instance
        new_review = Review(track_id=track.id,track_review=review,user=current_user)
        new_review.save_review()
        return redirect('/charts/tracks/{track_id}'.format(track_id=trackId))
    return render_template('charts-detail.html',track=track,reviews=reviews,review_form=review_form)

@main.route('/charts/albums/<albumid>')
@login_required
def albums_tracks(albumid):
    albums = getTracksForAlbums(albumid)
    
    return render_template('album-detail.html',albums=albums)

@main.route('/user/<userid>/<uname>')
@login_required
def profile(userid,uname):
   user = User.query.filter_by(username = uname).first()
   title='User Profile'
   reviews = Review.get_reviews_by_user(userid)
   
   if user is None:
      abort(404)
   return render_template("profile/profile.html", title = title,reviews=reviews,user=user)


@main.route('/user/<userid>/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname,userid):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username,userid=user.id))

    return render_template('profile/update.html',form =form)

@main.route('/user/<userid>/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname,userid):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.prof_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname,userid=userid))

# @main.route('/charts/playlists')
# def playlists():
#     allArtists = getChartPlaylists()

#     return render_template('playlists.html',playlists=allArtists)
