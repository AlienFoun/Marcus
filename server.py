from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from reply import reply_output
from study import update_problems_dict
from helper import sanitizer

app = Flask(__name__)
CORS(app)

api = Api(app)
application = app

host = 'marcus-program.ru'
port = 4000


class Study(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_text")
        parser.add_argument("user_tags", action='append')
        params = parser.parse_args()

        sanitized_text = sanitizer(params['user_text'])

        update_problems_dict(sanitized_text, params['user_tags'])


class Reply(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_text")
        params = parser.parse_args()
        print(params['user_text'])

        input_text = params['user_text']
        sanitized_input_text = sanitizer(input_text)

        output_list = reply_output(sanitized_input_text)

        return output_list


api.add_resource(Study, "/study", "/study/")
api.add_resource(Reply, "/reply", "/reply/")

if __name__ == '__main__':
    app.run(host=host, port=port)
