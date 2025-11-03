from flask import *
from . import dash_bp
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.Useless
collection = db.Working

@dash_bp.route('/', methods=['POST', 'GET'])
def Index():
    if request.method == 'POST':
        name = request.form['name']
        data = {
            "username":name
        }
        collection.insert_one(data)
        print(name)
        return redirect(url_for('dashboard.Index'))
    return render_template("index.html")