#NexmoCalendar

About Nexmo you can find Nexmo tutorial
or I write something Nexmo example on Python-Kivy-Example.

This is a project in NISRA-Hackathon.

## Flask

If you want to run flask with python in your computer,
you have to install flask on virtual environment.

In terminal:
Find folder venv then

```
. venv/bin/activate
```

Now you can run flaskr.py with flask.

Run it on your server give app.run(host='0.0.0.0')

## SQLite3

We use schema.sql to create flaskr.db
You can define the data what you want in .sql

```
drop table if exists entries;
create table entries(
  id integer primary key autoincrement,
  Event text not null,
  SDate date not null,
  STime time not null,
  FDate date not null,
  FTime time not null,
  Location text not null,
  Note text
);
```

And make initialize in python

```python
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
```

You can watch more detail on Flask Tutorial.

```
values (?,?,?,?,?,?,?)
```
Help you to protect SQL Injection when using database
