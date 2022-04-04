# pythonWebApp

Python Web Application

## TODO

<ol>
<li>Basic setup: Web Application "/" route - DONE IN HEROKU</li>
<li>Plan Web APP and API</li>
<li>Build and serve web app from "/" route</li>
<li>Authentication - API "/api/core/auth" and "/login" page</li>
<li>Dashboard</li>
<li>Core - generate report</li>
<li>Core - generate plot</li>
<li>Registration</li>
<li>Landing Page</li>
<li>Forgot password</li>
</ol>

<hr>

### Application

Main python file : ``app.py``

Requirements :

```
click==8.1.2
colorama==0.4.4
Flask==2.1.1
gunicorn==20.1.0
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
waitress==2.1.1
Werkzeug==2.1.1
```

Procfile
``web: gunicorn app:app``

Runtime
``python-3.10.2``

### Deployment

#### Heroku

<ol>
<li>heroku login</li>
<li>git add .</li>
<li>git commit -m < message > </li>
<li>git push origin main</li>
<li>git push heroku main</li>
</ol>