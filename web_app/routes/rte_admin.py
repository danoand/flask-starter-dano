import os

from flask import (Blueprint,
    jsonify,
    request,
    render_template,
    flash,
    redirect)

from web_app.models_data.models import db, Tweet

# API Key
API_KEY = os.environ.get('FL_APP_SECRET_KEY')

# Define admin_routes 
admin_routes = Blueprint("admin_routes", __name__)

# Import the db object for use in this module
from web_app.models_data.models import db 

# Define the Blueprint instance for this module
@admin_routes.route("/admin/db/dump_tweets")
def dump_tweets():
    # Grab URI arguments
    if len(request.args) == 0:
        # Expecting an argument but its missing
        print(f"ERROR: missing URI argument")
        flash("Missing URI argument", "danger")
        return redirect("/view_error")

    if "api_key" not in dict(request.args):
        print(f"ERROR: missing API Key. Reset database not allowed")
        flash("Missing API Key. Please check and try again", "danger")
        return redirect("/db_reset")

    if request.args["api_key"] != API_KEY:
        print(f"WARN: invalid API Key. Reset database not allowed")
        flash("Invalid API Key. Please check and try again", "danger")
        return redirect("/db_reset")
    
    # Fetch the tweets from the database
    my_tweets = Tweet.query().all()
    for twt in my_tweets:
        print(twt.full_text)

