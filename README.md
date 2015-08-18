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
`DATABASE_URL` environment variable. Bootstrap Admin replaces the default
admin templates with a responsive version. Daterange Filter adds a datepicker
filter when viewing the admin list view for models.

Installation
------------

```
$ pip install -r requirements.txt
$ python manage.py migrate
```

Running
-------

```
python manage.py runserver
```


Licensing
---------

[MIT](http://opensource.org/licenses/MIT)
