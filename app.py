from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, AnalysisModel

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config["DEBUG"] = True

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@postgres:5432/apiV2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# BAD code - Just for testing database is working. Will need to think of a better way to insert data (MYSQL query?)
with app.app_context():
    db.session.add(AnalysisModel(timestamp='2021-12-01', category='loc', value=70))
    db.session.commit()


@app.route('/', methods=['GET'])
def get_data():
    # GET endpoint to show values for a given domain
    data = AnalysisModel.query.all()

    labels = []
    category_dict = {"loc": [], "flake8": [], "noqa": [], "mod_size": [], "coverage": []}

    for d in data:
        formatted_time = d.timestamp.strftime('%d-%m-%Y')
        if formatted_time not in labels:
            labels.append(formatted_time)
        category_dict[d.category].append(d.value)
    return render_template('table.html', labels=labels, category_dict=category_dict)


if __name__ == '__main__':
    app.run()
