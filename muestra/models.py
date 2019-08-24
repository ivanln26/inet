from main import db


class Muestra(db.Model):

    id = db.Column(db.DateTime, primary_key=True)
    i = db.Column(db.Float)
    v = db.Column(db.Float)
    w_d = db.Column(db.String(10))
    w_s = db.Column(db.Float)

    def __repr__(self):
        return '<Muestra %r>' % self.id
