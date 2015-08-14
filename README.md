Blue Engine Student Tracker (BEST)
==================================

[Blue Engine]( http://blueengine.org/ )

This is a [Django]( https://www.djangoproject.com/ ) application to
allow Blue Engine Teaching Assistants (BETAs) to track student progress.

Dependencies
------------

See requirements.txt

Nothing crazy, basically just Django, gunicorn. SQLite should be fine
for development, and will be used by default. To use PostgreSQL, set the
`DATABASE_URL` environment variable.

Installation
------------

```
$ pip install -r requirements.txt
$ python manage.py migrate
```

Running
-------

```
gunicorn blueengine.wsgi --log-file -
```


Licensing
---------

[MIT](http://opensource.org/licenses/MIT)
