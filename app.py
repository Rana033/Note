from flask import Flask
from flask import Blueprint, render_template, url_for
from main import main_bp
from database import Note,engine

#######################################################################
app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


################################################################

app.register_blueprint(main_bp)