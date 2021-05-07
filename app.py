from flask import Flask, render_template, request

from util import get_retail_services, get_associate_services, get_service, get_segments, get_main_content

app = Flask('app', static_url_path='/static')
app.secret_key = 'very very secret'


@app.route('/')
def index():
    data = get_main_content()
    return render_template('index.html',
                           business=data['business'],
                           services=data['service'],
                           associate=data['associate'])


@app.route('/services')
def services():
    return render_template('services.html', services=get_retail_services())


@app.route('/service')
def service():
    return render_template('service.html', service=get_service(request.args.get('id')))


@app.route('/segments')
def segments():
    return render_template('segments.html', segments=get_segments())


@app.route('/partners')
def partners():
    return render_template('partners.html', services=get_associate_services())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
