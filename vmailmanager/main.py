#! /usr/bin/env python3

from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('vmailmanager.cfg')

app.config['SECRET_KEY'] = config['general']['session_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://{}:{}@{}/{}'.format(
    config['database']['db_user'],
    config['database']['db_password'],
    config['database']['db_location'],
    config['database']['db_name']
)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return redirect("/admin")


from vmailmanager.admin_views import *
from vmailmanager.models import *

admin = Admin(app, name='Mail Admin', template_mode='bootstrap4')
admin.add_view(VirtualDomainAdmin(VirtualDomain, db.session))
admin.add_view(VirtualUserAdmin(VirtualUser, db.session))
admin.add_view(VirtualAliasesAdmin(VirtualAliases, db.session))
