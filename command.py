import click
import requests
from flask_sqlalchemy import SQLAlchemy
from main import app
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Muestra(db.Model):
    id = db.Column(db.DateTime, primary_key=True)
    i = db.Column(db.Float)
    v = db.Column(db.Float)
    w_d = db.Column(db.String(10))
    w_s = db.Column(db.Float)

    def __repr__(self):
        return '<Muestra %r>' % self.id

r = requests.get('http://192.168.30.199:9090/')
a = r.json()

@click.command()
def hello():
    db.create_all()

    for k, v in a.items():
        id = datetime.strptime(k, '%Y-%m-%d %H:%M:%S')
        muestra = Muestra.query.get(id)
        if muestra is None:
            muestra = Muestra(id=id, i=v['i'], v=v['v'], w_d=v['w_d'], w_s=v['w_s'])
            db.session.add(muestra)
            db.session.commit()
            click.echo(muestra)
    click.echo(Muestra.query.order_by(Muestra.id).all()[:24])

if __name__ == '__main__':
    hello()
