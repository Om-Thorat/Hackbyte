from flask import Flask, send_from_directory
from datetime import datetime
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from pymongo.mongo_client import MongoClient
from dotenv import find_dotenv, load_dotenv
from os import environ as env
from bson import json_util
import certifi

from Db.Posts import getPosts,InsertPost,searchPost
from Db.Organisations import getOrganisations
from Db.User import InsertUser
from Db.Ai import getKeywords,getsimilarCompanies,getsimilarTags
from flask import request


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

uri = env.get('MONGO_URI');
print(uri)
client = MongoClient(uri, tlsCAFile=certifi.where())


# To expose the main page
@app.route('/')
def root():
    # test_db(client)
    return send_from_directory('./client/dist', 'index.html')


@app.route('/posts')
def posts():
    posts = getPosts(client.hackdb,session.get('user'))
    return json.loads(json_util.dumps(posts))

@app.route('/AllOrganisations')
def Organisations():
    Organisations = getOrganisations(client.hackdb)
    return json.loads(json_util.dumps(Organisations))

@app.route('/user')
def user():
    if(session.get('user')):
        # call a function to get user data
        # print(session.get('user'))
        InsertUser(session.get('user'),client.hackdb)
        
    return session.get('user') or 'No'

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/search", methods=["GET"])
def search():
    q = request.args.get("q")
    posts = searchPost(client.hackdb,q)
    return json.loads(json_util.dumps(posts))

@app.route("/addpost", methods=["GET"])
def addpost():
    title = request.args.get("title")
    body = request.args.get("body")
    Ptype = request.args.get("type")
    tags = request.args.get("tags")
    tags = list(set(tags.split(',') + getKeywords(body)));
    
    InsertPost(client.hackdb, title, body, ','.join(tags), Ptype ,session.get('user'))
    
    return "Post added successfully"


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

# To expose all the assets 
@app.route('/<path:path>')
def assets(path):
    return send_from_directory('./client/dist',path)

# Backend functions to fetch
@app.route('/time')
def gettime():
    return str(datetime.now().strftime("%H:%M:%S"))

# if __name__ == "__main__":
#     app.run(debug=True)