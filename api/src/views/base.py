from flask import jsonify


class View:
    @staticmethod
    def format_response(data, status=200):
        return jsonify(status=status, data=data)

    def render():
        raise NotImplementedError