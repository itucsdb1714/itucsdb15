from flask import Flask, Blueprint, render_template
from flask import current_app

from datetime import datetime

site = Blueprint('site', __name__)


@site.route('/')
def login_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('login_page.html', day_name=day,signedin=False)


@site.route('/home')
def home_page():
    now = datetime.now()
    day = now.strftime('%A')
    return render_template('home_page.html', day_name=day,signedin=True,message = True)


