from flask import jsonify


class View:
    @staticmethod
    def format_response(data, status_code=200):
        response = jsonify(data=data)
        response.status_code = status_code

        return response

    def get():
        raise NotImplementedError

    def post():
        raise NotImplementedError
