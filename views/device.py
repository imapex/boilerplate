from flask import render_template


def device_list():
    return render_template('device-list.html')
