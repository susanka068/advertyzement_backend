from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema, Banks

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'gql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.route('/')
def home():
    return "<h1>Hello, Welcome to advertyzement backend made my susanka068.</h1> <br/> <h2>append '/gql' at the end of this URL to visit the graphql interface</h2>"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()