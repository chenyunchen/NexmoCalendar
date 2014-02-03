import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

app = Flask(__name__)
app.config.update(dict(
   DATABASE = '/tmp/flaskr.db',
   DEBUG = True,
   SECRET_KEY = 'development key',
   USERNAME = 'admin',
   PASSWORD = 'default',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource("schema.sql") as f:
      db.cursor().executescript(f.read())
    db.commit()

@app.before_request
def before_request():
  g.db = connect_db()
@app.teardown_request
def teardown_request(exception):
  g.db.close()

@app.route('/')
def show_entries():
  cur = g.db.execute('select Event, SDate, STime, FDate, FTime , Location, Note from entries order by id desc')
  entries = [dict(Event=row[0], SDate=row[1], STime=row[2], FDate=row[3], FTime=row[4], Location=row[5], Note=row[6]) for row in cur.fetchall()]
  return render_template('show_entries.html', entries=entries)
@app.route('/add',methods=['POST'])
def add_entry():
  if not session.get('logged_in'):
    abort(401)
  g.db.execute('insert into entries (Event, SDate, STime, FDate, FTime, Location, Note) values (?,?,?,?,?,?,?)',
              [request.form['Event'], request.form['SDate'], request.form['STime'], request.form['FDate'], request.form['FTime'], request.form['Location'], request.form['Note']])
  g.db.commit()
  flash('New entry was successfully posted')
  return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      error = 'Invalid username'
    elif request.form['password'] != app.config['PASSWORD']:
      error = 'Invalid username'
    else:
      session['logged_in'] = True
      flash('You were logged in')
      return redirect(url_for('show_entries'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('You were logged out')
  return redirect(url_for('show_entries'))

if __name__ == '__main__':
  init_db()
  app.run(host='0.0.0.0')
