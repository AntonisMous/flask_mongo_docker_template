from flask import request, render_template, redirect, url_for


def init_routes(app):

    @app.route('/')
    def index():
        return "Hello WE!"
