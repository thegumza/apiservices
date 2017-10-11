import sqlalchemy
from flask import jsonify
from flask import Flask
from sqlalchemy import text

import db

app = Flask(__name__)
engine = sqlalchemy.create_engine(db.DB.web_db())


@app.route('/rubber_price/<name>', methods=['GET'])
def get_rubber_price(name):
    prices = engine.execute(text("""
        SELECT * FROM {}
        """.format(name))).fetchall()
    return jsonify({'data': [dict(i) for i in prices]})


@app.route('/rubber_news/<page>', methods=['GET'])
def get_rubber_price(page):
    offset = (int(page) - 1) * 30
    prices = engine.execute(text("""
        SELECT * FROM rubber_news
        LIMIT :offset, 30
        """), offset=offset).fetchall()
    return jsonify({'data': [dict(i) for i in prices]})


app.run(host='0.0.0.0')
