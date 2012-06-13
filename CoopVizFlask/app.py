from flask import Flask, render_template, redirect, url_for
from flask_peewee.auth import Auth
from flask_peewee.db import Database
from flask_peewee.admin import Admin
from werkzeug import secure_filename


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = Database(app)
auth = Auth(app, db)
admin = Admin(app, auth)

import models
@app.route('/')
def main():
    return "Hola Mundo"

if __name__ == "__main__":
    auth.register_admin(admin)
    admin.register(models.Cooperativa)
    admin.register(models.Federacion)
    admin.register(models.CoopFederacion)
    admin.setup()
    app.run()





