from flask.json import jsonify
from flask_restful import Resource

from App.models import Hello


class Hellos(Resource):
    def get(self):
        hellos=Hello.query.all()
        for hello in hellos:
            print(hello.name)
            print(type(hello))
        data={
            'msg' : '我是get',
        }
        json=jsonify(data)
        print(json)
        print(type(json))
        return json

    def post(self):
        data = {
            'msg': '我是post',
        }
        return jsonify(data)

    def delete(self):
        data = {
            'msg': '我是delete',
        }
        return jsonify(data)
