from flask import Flask
from init.database import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS

app = Flask(__name__)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

environment_variable = 'SETTINGS'
app.config.from_object('settings.base')
CORS(app, support_credentials=True)
db.init_app(app)

def init():
    with app.app_context():
        from init.jwt_init import jwt
        jwt.init_app(app)

        from apps.sparks.urls import sparks
        app.register_blueprint(sparks)

        from apps.users.urls import users
        app.register_blueprint(users)

init()


if __name__ =='__main__':
    manager.run()
    app.run(host='0.0.0.0', threaded=False)
