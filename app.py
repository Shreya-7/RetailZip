from flask import Flask, render_template, request, redirect, make_response, jsonify

import json
from datetime import datetime
from util import get_next_request_number, get_data, get_retail_services, get_associate_services, get_service, get_segments, get_main_content, get_about_us, misc_error, remove_field
from email_util import send_email

app = Flask('app', static_url_path='/static')
app.secret_key = 'veryverysecretisntitormaybeitis'

if __name__ == '__main__':
    app.run(host='0.0.0.0')


@app.route('/contact_form', methods=["POST"])
def contact_form():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    try:
        json_content = get_data('json/clients.json')

        client_details = request.form.to_dict()
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        client_details['timestamp'] = current_time

        request_number = get_next_request_number()

        if client_details['type'] == '0':

            client_details.pop('type')
            json_content['short'][request_number] = client_details
        else:
            client_details.pop('country')
            client_details.pop('type')
            multi_keys = ['ownership', 'vertical', 'service', 'associate']
            for key in multi_keys:
                client_details[key] = ', '.join(request.form.getlist(key))
            json_content['detail'][request_number] = client_details

        json.dump(json_content, open('json/clients.json', 'w'))

        send_email(client_details, request_number)

        return make_response(jsonify({
            'message': 'Thank you for choosing RetailZip. You have successfully made a consultation request. Please check your email for further details :)'
        }), 200)

    except Exception as e:
        print(e)
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
                           services=data['service'],
                           associate=data['associate'])


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
        Opens the page for a particular service based on its ID (be it retail or associate)
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


@app.route('/partners')
@misc_error
def partners():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        print('Redirecting...')
        return redirect(url, code=code)
    return render_template('partners.html', services=get_associate_services())


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
                           services=get_retail_services(),
                           associate=get_associate_services())
