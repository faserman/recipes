from flask_jwt import JWT

jwt = JWT()

@jwt.authentication_handler
def authentication(username, password):
    return
