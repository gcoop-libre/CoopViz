from flask import Flask, render_template, redirect, url_for, jsonify
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
@app.route('/nodos.json')
def main():
    return jsonify(models.generar_diccionario_nodos())

@app.route('/')
def main():
    return render_template('test.html', json_data=models.generar_diccionario_nodos()) 


if __name__ == "__main__":
    auth.register_admin(admin)
    admin.register(models.Cooperativa)
    admin.register(models.Federacion)
    admin.register(models.CoopFederacion)
    admin.setup()
    app.run(host='0.0.0.0')





