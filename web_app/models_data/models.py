# Import ORM and database migrations packages/modules
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate    import Migrate 

# Create a SQLAlchemy database object
db = SQLAlchemy()
# Create a migration object
migrate = Migrate()

# Define: User class
class User(db.Model):
    id              = db.Column(db.BigInteger, primary_key=True)
    screen_name     = db.Column(db.String(128), nullable=False)
    name            = db.Column(db.String)
    location        = db.Column(db.String)
    followers_count = db.Column(db.Integer)

# Define: Tweet class 
class Tweet(db.Model):
    id          = db.Column(db.BigInteger, primary_key=True)
    user_id     = db.Column(db.BigInteger, db.ForeignKey("user.id"))
    full_text   = db.Column(db.String(512))
    embedding   = db.Column(db.PickleType) # used to serialize a Python object (and store in the db)

    user = db.relationship("User", backref=db.backref("tweets", lazy=True))

# rows_to_maps parses db rows to json
def rows_to_maps(db_rows):
    """
    rows_to_json parses db rows into json documents
    """

    # Define a return set
    parsed_rows = []

    # Iterate through db row objects
    for row in db_rows:
        parsed_row = row.__dict__
        del parsed_rows["_sa_instance_state"]

        # Add a dict/map to the return set
        parsed_rows.append(parsed_row)

    # Return list of dicts (rows)
    return parsed_rows
