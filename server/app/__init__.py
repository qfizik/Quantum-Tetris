import os
from flask import Flask, request
from flask_cors import CORS
from . import db
from . import game
from app.player import Player

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Commented out so that we can run everything without a db for now
    db.init_app(app)
    app.register_blueprint(game.bp)
    app.add_url_rule('/', endpoint='game')


    player=Player(db)
    @app.route('/api/createPlayer', methods=['POST'])
    def createPlayer():
        if request.method == 'POST':
            params=request.get_json()
            username = params['username']
            hiscore = params['hiscore']
            response = player.createPlayer(username, hiscore)
            return response
        print("CreatePlayer")
        return None


    @app.route('/api/fetchPlayer/', methods=['GET'])
    def fetchPlayer(username=None):
        if request.method == 'GET':
            username = request.args.get('username', default= None, type= str)
            response = player.fetchPlayer(username)
            return response
        print("FetchPlayer")
        return None

    @app.route('/api/deletePlayer', methods=['DELETE'])
    def delete():

        return player

    return app
