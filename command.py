from datetime import datetime

import click
import requests

from muestra.models import Muestra, db

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

if __name__ == "__main__":
    hello()
