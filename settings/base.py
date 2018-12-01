SECRET_KEY = 'blah'
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(**{
    'NAME': 'recipes',
    'USER': 'faserman',
    'PASSWORD': 'password',
    'HOST': '127.0.0.1',
    'PORT': '5432'
})

CORS_HEADERS = 'X-Requested-With, Content-Type'