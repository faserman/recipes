from datetime import timedelta



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


JWT_EXPIRATION_DELTA = timedelta(days=365)
JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)
JWT_VERIFY_CLAIMS = ['signature', 'exp', 'nbf', 'iat']
JWT_REQUIRED_CLAIMS = ['exp', 'iat', 'nbf']
JWT_AUTH_HEADER_PREFIX = 'JWT'
JWT_AUTH_URL_RULE = '/users/auth'
JWT_AUTH_USERNAME_KEY = 'email'
JWT_AUTH_PASSWORD_KEY = 'password'