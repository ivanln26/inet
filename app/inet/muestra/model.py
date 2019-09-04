from sqlalchemy import Column, DateTime, Float, String

from app import db


class Muestra(db.Model):

    id = Column(DateTime, primary_key=True)
    i = Column(Float)
    v = Column(Float)
    w_d = Column(String(10))
    w_s = Column(Float)

    def __repr__(self):
        return '<Muestra %r>' % self.id
