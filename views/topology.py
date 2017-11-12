from flask import render_template
import json


def get_topology_data():
    topologyData = {
        "nodes": [
            {"id": 100, "x": 410, "y": 100, "name": "12K-1"},
            {"id": 101, "x": 410, "y": 280, "name": "12K-2"},
            {"id": 102, "x": 660, "y": 280, "name": "Of-9k-03"},
            {"id": 103, "x": 660, "y": 100, "name": "Of-9k-02"},
            {"id": 104, "x": 180, "y": 190, "name": "Of-9k-01"}
        ],
        "links": [
            {"source": 0, "target": 1},
            {"source": 1, "target": 2},
            {"source": 1, "target": 3},
            {"source": 4, "target": 1},
            {"source": 2, "target": 3},
            {"source": 2, "target": 0},
            {"source": 3, "target": 0},
            {"source": 3, "target": 0},
            {"source": 3, "target": 0},
            {"source": 0, "target": 4},
            {"source": 0, "target": 4},
            {"source": 0, "target": 3}
        ]
    }
    return topologyData

def topology():
    return render_template('topology.html', topo=get_topology_data())
