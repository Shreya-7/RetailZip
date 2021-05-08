from flask import Flask, render_template, request

from util import get_retail_services, get_associate_services, get_service, get_segments, get_main_content, get_about_us, misc_error

app = Flask('app', static_url_path='/static')
app.secret_key = 'veryverysecretisntitormaybeitis'

if __name__ == '__main__':
    app.run(host='0.0.0.0')


@app.route('/')
@misc_error
def index():
    data = get_main_content()
    return render_template('index.html',
                           business=data['business'],
                           services=data['service'],
                           associate=data['associate'])


@app.route('/services')
@misc_error
@misc_error
def services():
    return render_template('services.html', services=get_retail_services())


@app.route('/service')
@misc_error
def service():
    """
        Opens the page for a particular service based on its ID (be it retail or associate)
    """
    return render_template('service.html', service=get_service(request.args.get('id')))


@app.route('/verticals')
@misc_error
def segments():
    return render_template('segments.html', segments=get_segments())


@app.route('/partners')
@misc_error
def partners():
    return render_template('partners.html', services=get_associate_services())


@app.route('/about')
@misc_error
def about():
    return render_template('about.html', content=get_about_us())


@app.route('/contact')
@misc_error
def contact():
    return render_template('contact.html')
