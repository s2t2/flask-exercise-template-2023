

import os
from dotenv import load_dotenv

from flask import Flask
from authlib.integrations.flask_client import OAuth

#from app.spreadsheet_service import SpreadsheetService

from web_app.routes.home_routes import home_routes
from web_app.routes.product_routes import product_routes
from web_app.routes.auth_routes import auth_routes
from web_app.routes.user_routes import user_routes

load_dotenv()


APP_ENV = os.getenv("APP_ENV", default="development") # IMPORTANT: set to "production" in production
APP_VERSION = os.getenv("APP_VERSION", default="v0.0.1") # update upon new releases
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # IMPORTANT: override in production

# for google oauth login:
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# for google analytics:
GA_TRACKER_ID = os.getenv("GA_TRACKER_ID", default="G-OOPS")


def create_app():

    #
    # INIT
    #

    app = Flask(__name__)

    #
    # CONFIG
    #

    app.config["APP_ENV"] = APP_ENV
    app.config["APP_VERSION"] = APP_VERSION

    # for flask flash messaging:
    app.config["SECRET_KEY"] = SECRET_KEY

    # for client-side google analytics:
    app.config["GA_TRACKER_ID"] = GA_TRACKER_ID

    # set timezone to mimic production mode when running locally:
    os.environ["TZ"] = "UTC"

    #
    # AUTH
    #

    oauth = OAuth(app)
    oauth.register(
        name="google",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        #authorize_params={"access_type": "offline"} # give us the refresh token! see: https://stackoverflow.com/questions/62293888/obtaining-and-storing-refresh-token-using-authlib-with-flask
    )
    app.config["OAUTH"] = oauth

    #
    # SERVICES
    #

    #app.config["SPREADSHEET_SERVICE"] = SpreadsheetService()

    #
    # ROUTES
    #

    app.register_blueprint(home_routes)
    app.register_blueprint(product_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(user_routes)

    return app



if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
