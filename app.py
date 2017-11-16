from flask import Flask, render_template, request
from flask_restful import Api
from views.topology import topology
from views.dashboard import dashboard
from views.device import device_list
from views.patterns import patterns
from api.device import Device
from api.topology import Topology

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(Device, '/api/device')
api.add_resource(Topology, '/api/topology')
app.add_url_rule('/topology', endpoint='topology-view', view_func=topology)
app.add_url_rule('/device', endpoint='device-list', view_func=device_list)
app.add_url_rule('/dashboard', endpoint='dashboard', view_func=dashboard)
app.add_url_rule('/patterns', endpoint='patterns', view_func=patterns)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
