from sys import exit
from mongoengine import connect
from pymongo.errors import ServerSelectionTimeoutError


class MongodbHandler(object):

    def __init__(self):
        self.connection = None

    def init_app(self, app):
        self.connection = connect(host=app.config['MONGO_URI'])
        try:
            app.logger.info("Trying to connect to mongodb ...")
            self.connection.server_info()
        except ServerSelectionTimeoutError:
            app.logger.critical("Cannot connect to mongodb. Will exit")
            exit(1)
        app.logger.info("Successfully connected to mongodb..")
        return self.connection

    def get_connection(self):
        return self.connection
