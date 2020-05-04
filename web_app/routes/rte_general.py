from flask import (Blueprint,
    jsonify,
    request,
    render_template,
    flash,
    redirect)

# Define admin_routes 
general_routes = Blueprint("general_routes", __name__)

# Define the Blueprint instances for this module
@general_routes.route("/view_error")
def view_error():
    return render_template("view_error.html") # put html file in templates folder by convention



