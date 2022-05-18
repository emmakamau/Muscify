from flask import render_template,request,redirect,url_for,abort
from . import main

@main.route('/')
def index(): 
   title="Homepage"
   
   return render_template('index.html',title=title)