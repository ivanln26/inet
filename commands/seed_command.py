from datetime import datetime

import click
from flask.cli import with_appcontext
import requests

@click.command()
@click.option('--host', default='localhost')
@click.option('--port', default='9090')
@with_appcontext
def seed_command(host, port):
    from app import db
    from app.inet.muestra import Muestra

    req = requests.get(f'http://{host}:{port}/')
    data = req.json()
    db.create_all()

    for k, v in data.items():
        id = datetime.strptime(k, '%Y-%m-%d %H:%M:%S')
        muestra = Muestra.query.get(id)
        if muestra is None:
            muestra = Muestra(id=id, i=v['i'], v=v['v'], w_d=v['w_d'], w_s=v['w_s'])
            db.session.add(muestra)
            click.echo(muestra)
    db.session.commit()


if __name__ == "__main__":
    seed_command()
