from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import muestra

app = Flask(__name__)

app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.register_blueprint(muestra.bp)
    app.run(port=8000, debug=True)
