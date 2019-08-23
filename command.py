import click
import requests

r = requests.get('http://ec2-54-233-198-25.sa-east-1.compute.amazonaws.com/rest/group/')
a = r.json()
@click.command()
def hello():
    click.echo(a)

if __name__ == '__main__':
    hello()
