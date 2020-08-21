import logging
from log4mongo.handlers import BufferedMongoHandler


class Logger(object):
    @staticmethod
    def init_app(app):
        handler = BufferedMongoHandler(host=app.config['MONGO_URI'],
                                       database_name=app.config['ENVIRONMENT'],
                                       capped=True,
                                       buffer_size=100,
                                       buffer_periodical_flush_timing=10.0,
                                       buffer_early_flush_level=logging.ERROR)

        handler.setLevel(app.config['LOGGING_LEVEL'])
        # Maybe ...
        # formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
        # handler.setFormatter(formatter)
        app.logger.addHandler(handler)
