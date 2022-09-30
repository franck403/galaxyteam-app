import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some tes
all = [
    {'id': 0,
     'title': 'The olympic',
     'author': 'Geoloup',
     'subjet': 'grec olympic and the a special animal',
     'year_published': '2022'},
    {'id': 1,
     'title': 'les chiens',
     'author': 'alan startor',
     'traduction ?': 'traduction from the english',
     'published': '2000'},
    {'id': 2,
     'title': 'youtube gilaxy04',
     'author': 'Gilaxy04',
     'video editor': 'Geoloup',
     'published': '2020'}
]
books = [
    {'id': 0,
     'title': 'les chiens',
     'author': 'alan startor',
     'traduction ?': 'traduction from the english',
     'published': '2000'},
]
revues = [
    {'id': 0,
     'title': 'The olympic',
     'author': 'Geoloup',
     'subjet': 'grec olympic and the a special animal',
     'year_published': '2022'}
]
youtube = [
  {'id': 0,
     'title': 'youtube gilaxy04',
     'author': 'Gilaxy04',
     'video editor': 'Geoloup',
     'published': '2020'}
]
info = [
  {'id': 0,
     'title': 'information',
     'author': 'Api made by gilaxy04',
     'video editor': 'Geoloup',
     'published': '2020'}
]

@app.route('/', methods=['GET'])
def home():
  return '''<h1p;9,,.éApi</h1>
<h2>Refenrage book API.</h2>
<h3>Made by gilaxy04.</h3>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/resources/all', methods=['GET'])
def api_all():
    return jsonify(all)

@app.route('/api/resources/revue')
def api_revue():
  return jsonify(revues)

@app.route('/api/resources/book')
def api_book():
  return jsonify(books)

@app.route('/api/resources/youtube')
def api_youtube():
  return jsonify(youtube)

class api():
  def run():
    app.run(host='0.0.0.0', port=8000)


app.run(host='0.0.0.0', port=8000)
