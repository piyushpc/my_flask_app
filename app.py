from flask import Flask, request, g, render_template
import sqlite3

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

DATABASE = 'mydatabase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    db = get_db()
    db.execute('INSERT INTO entries (name) VALUES (?)', [name])
    db.commit()
    return "Entry added!"

@app.route('/entries')
def show_entries():
    db = get_db()
    cur = db.execute('SELECT name FROM entries')
    entries = cur.fetchall()
    return render_template('entries.html', entries=entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
