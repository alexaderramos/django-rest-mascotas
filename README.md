# Api Animal Force Python

## First

Rename file `secret.json.example` to `secret.json `

And set environment variables

## Running locally

Install packages
```
pip install -r requirements/local.txt
```

To deploy the project, execute from terminal


```
python manage.py runserver
```

You can visit [http://localhost:8000](http://localhost:8000)

## Running production

Install packages
```
pip install -r requirements/prod.txt
```

Execute from terminal 

```
python .\manage.py runserver --settings=api_animalforce.prod
```

If you want to run python `manage.py runserver`, you must change the following files:

**manage.py**
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_animalforce.settings.prod')`

**wsgi.py**
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_animalforce.settings.prod')`


Now you can run from terminal

```
python manage.py runserver
```

You can visit [http://localhost:8000](http://localhost:8000)
