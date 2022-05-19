### Muscify
#### Description
An application where you can find all the song details (description, artist, albums and the video) online and also be able to download it and listen offline
### Technologies used
1. Python Flask
2. HTML( Jinja templates )
3. CSS3 and Boostrap for styling
4. PostgresSQL Database
### Installation
#### Prerequisites
* Make sure you have git and python3.7 or later installed in your pc.
* Also ensure that you have an IDE installed preferably Visual studio code,Atom,Pycharm or any other compatible IDE.
#### Cloning
* You can clone this repository by navigating into your desired directory in your machine and on the terminal type the following command:
```
1. git clone [https://github.com/emmakamau/Muscify.git]
2. Navigate to  Muscify by typing ```cd Muscify```
3. Create a Virtual environment by typing ```python3 -m venv --without-pip virtual```
4. Install all the dependencies specified in requirements.txt file by typing ``` pip install -r requirements.txt```
5.On the terminal run the following commands;
 * $ chmod +x start.sh
 * $ ./start.sh
```
#### Deployment environment
* Heroku
### Live Link
> The link to the live site is:
### Behaviour Driven Development
This focuses on how the site users will interact with the application.
1. A landing page with a background,navigation bar and a button to ask users to join.
2. Navigation bar has a four routes,Discover,SignIn and Join. To the left it has a logo(Muscify) that redirects to the home page when clicked.
3. The discover route has 4 route buttons for the charts,albums,Podcast and artist.
4. The Charts button directs the user to a route that displays all the charts from the Api.(A user can listen to the tracks through a redirect link in the charts information).
5. A user can add view reviews of the track and can also add their own reviews.
6. The albums button directs the user to a route that displays all the albums from the Api.
7. The Podcasts button directs the user to a route that displays all the podcasts from the Api.
8. The artist button directs the user to a route that displays some artists from the Api with their information.
9. The SignIn route from the navigation bar redirects a user to  welcome back page with a form to give their details and log into the system.
10. The Join button redirects a user to a sign up page with a form to register their details.
11. Once a user creates an account and logs in,they can view their profile and update their information.
### Test Driven Development
This focuses on methods being created and whether they pass prior designed tests.
* To run tests for this application run the the following command on the terminal:
  `$ python3 manage.py test`
### Reference
* [Music Deezer API for developers](https://developers.deezer.com/api)
### Known Bugs
* There are no known bugs yet.If you encounter one,feel free to reach out.
### Authors
1. Emmaculate Kamau(Scrum master)
2. Rachel Kemuma Oyondi.
3. Pauline Wafula.
4. Lorraine Chepkemoi.
5. Agnes Kingee.
6. Sharon Kemboi
## License
> [MIT License](license) this application's source code is free for any open source projects
> Copyright (c) 2022 **Emmaculate Kamau**