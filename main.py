from datetime import datetime

import click
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Muestra(db.Model):

    id = db.Column(db.DateTime, primary_key=True)
    i = db.Column(db.Float)
    v = db.Column(db.Float)
    w_d = db.Column(db.String(10))
    w_s = db.Column(db.Float)

    def __repr__(self):
        return f'<Muestra {self.id}>'


@click.command()
@click.option('--host', default='localhost')
@click.option('--port', default='9090')
def hello(host, port):
    r = requests.get(f'http://{host}:{port}/')
    a = r.json()
    db.create_all()

    for k, v in a.items():
        id = datetime.strptime(k, '%Y-%m-%d %H:%M:%S')
        muestra = Muestra.query.get(id)
        if muestra is None:
            muestra = Muestra(id=id, i=v['i'], v=v['v'], w_d=v['w_d'], w_s=v['w_s'])
            db.session.add(muestra)
            db.session.commit()
            click.echo(muestra)


@app.route('/')
def index():
    data = Muestra.query.order_by(Muestra.id.desc()).all()[:144]
    return render_template('index.html', data=data)

if __name__ == "__main__":
    # hello()
    app.run(port=8000, debug=True)
