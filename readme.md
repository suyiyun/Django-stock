# Installation
```
pip install django django-apscheduler yfinance tqdm keras sklearn tensorflow
```

check installation by 
```
pip freeze
```

migrate all the databases
```
python manage.py migrate 
```
or use this if database/ table already existed
python manage.py migrate --fake


# Quick start
> start server
```
python manage.py runserver
```
