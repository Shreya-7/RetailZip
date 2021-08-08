from flask import Flask, render_template, request, redirect, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

import json
import os
import traceback
import re
from datetime import datetime
from util import get_next_request_number, get_data, get_retail_services, get_service, get_segments, get_main_content, get_about_us, misc_error
from email_util import send_email

app = Flask('app', static_url_path='/static')
app.secret_key = 'veryverysecretisntitormaybeitis'

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Short(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_number = db.Column(db.String(10), nullable=False, default="RZ")
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(15), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.request_number = kwargs["request_number"]
        self.number = kwargs["number"]
        self.message = kwargs["message"]
        self.timestamp = kwargs["timestamp"]
        self.name = kwargs["name"]

    def __repr__(self):
        return '<{} - {} - {}>'.format(self.request_number, self.name, self.email)


class Detail(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    request_number = db.Column(db.String(10), nullable=False, default="RZ")
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(15), nullable=False)
    alt_number = db.Column(db.String(15), nullable=True)
    message = db.Column(db.String(500), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    firm = db.Column(db.String(80), nullable=True)
    ownership = db.Column(db.String(100), nullable=False)
    vertical = db.Column(db.String(500), nullable=False)
    services = db.Column(db.String(500), nullable=False)

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.request_number = kwargs["request_number"]
        self.number = kwargs["number"]
        self.timestamp = kwargs["timestamp"]
        self.name = kwargs["name"]
        self.address = kwargs["address"]
        self.state = kwargs["state"]
        self.city = kwargs["city"]
        self.pincode = kwargs["pincode"]
        self.ownership = kwargs["ownership"]
        self.vertical = kwargs["vertical"]
        self.services = kwargs["service"]

        self.alt_number = kwargs["alt_number"] if "alt_number" in kwargs.keys(
        ) else 0
        self.firm = kwargs["firm"] if "firm" in kwargs.keys(
        ) else 0
        self.message = kwargs["message"] if "message" in kwargs.keys(
        ) else 0

    def __repr__(self):
        return '<{} - {}>'.format(self.request_number, self.name, self.email)


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')


@app.route('/contact_form', methods=["POST"])
def contact_form():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    try:

        client_details = request.form.to_dict()
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        client_details['timestamp'] = current_time

        if client_details['type'] == '0':

            client_details.pop('type')

            client_details['request_number'] = get_next_request_number(Short, Detail)
            entry = Short(**client_details)

            db.session.add(entry)
            db.session.commit()
        else:
            client_details.pop('country')
            client_details.pop('type')
            multi_keys = ['ownership', 'vertical', 'service', 'associate']
            for key in multi_keys:
                client_details[key] = ', '.join(request.form.getlist(key))

            client_details['request_number'] = get_next_request_number(Short, Detail)
            entry = Detail(**client_details)

            db.session.add(entry)
            db.session.commit()

        send_email(client_details, client_details['request_number'])

        return make_response(jsonify({
            'message': 'Thank you for choosing RetailZip. You have successfully made a consultation request. Please check your email for further details :)'
        }), 200)

    except Exception as e:
        print(traceback.print_exc())
        return make_response(jsonify({
            'error': 'An error occured while making the request. Please try again later or directly reach out to us at manish@retailzip.in'
        }), 400)


@app.route('/')
@misc_error
def index():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    data = get_main_content()
    return render_template('index.html',
                           business=data['business'],
                           services=data['service'])


@app.route('/services')
@misc_error
def services():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    return render_template('services.html', services=get_retail_services())


@app.route('/service')
@misc_error
def service():
    """
        Opens the page for a particular service based on its ID
    """
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    id = request.args.get('id')
    return render_template('service.html', service=get_service(id), id=id[0])


@app.route('/verticals')
@misc_error
def segments():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    return render_template('segments.html', segments=get_segments())


@app.route('/about')
@misc_error
def about():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    return render_template('about.html', content=get_about_us())


@app.route('/contact')
@misc_error
def contact():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    return render_template('contact.html')


@app.route('/consult')
@misc_error
def consult():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    return render_template('consult.html',
                           business=get_segments(),
                           services=get_retail_services())
