from http.server import HTTPServer, BaseHTTPRequestHandler
from reply import reply_output
import json

hostname = 'localhost'
port = 4000


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        input_data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()

        input_text = json.loads(input_data)

        output_list = reply_output(input_text)
        output_data = json.dumps(output_list)

        self.wfile.write(output_data.encode('utf-8'))


httpd = HTTPServer((hostname, port), SimpleHTTPRequestHandler)
httpd.serve_forever()
