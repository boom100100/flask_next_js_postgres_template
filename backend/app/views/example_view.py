from flask.views import MethodView
from flask import jsonify


class ExampleView(MethodView):
    """The API landing page."""

    def get(self, id: str):
        """Get the example."""

        response = jsonify({'data': int(id)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
