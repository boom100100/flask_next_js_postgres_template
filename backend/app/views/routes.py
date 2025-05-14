from flask import Blueprint
from app.views import ExampleView, ExamplesView


app_blueprint = Blueprint('app', __name__)
api_v1_blueprint = Blueprint('api_v1', __name__)

api_v1_blueprint.add_url_rule("/examples", view_func=ExamplesView.as_view("examples"), methods=['GET', 'POST', 'OPTIONS'])
api_v1_blueprint.add_url_rule("/examples/<id>", view_func=ExampleView.as_view("example"), methods=['GET', 'DELETE', 'PATCH',])
