from flask import current_app, jsonify, request
from flask.views import MethodView


class ExamplesView(MethodView):
    """The API landing page."""

    def get(self):
        """Get the examples."""

        response = jsonify({"data": "examples get data"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def post(self):
        """Post the examples."""

        response = jsonify({
            "data": {
                "sm": "post data",
                # note: js and python don't agree on variable name syntax; js is camelCase and python is snake_case.
                "received_body": request.json
            }
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def options(self):
        response = current_app.make_default_options_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        # setattr(response, "FLASK_CORS_EVALUATED", True) # I don't think this is necessary. If some unexpected post failures occur, I'll reactivate this snippet. But no dead code in production!
        return response