import json
import traceback
from flask import render_template, jsonify, session


def misc_error(my_function):
    """
        Miscellaneous Error Decorator
    """
    def wrap(*args, **kwargs):
        try:
            return my_function(*args, **kwargs)
        except:
            print(traceback.print_exc())
            return render_template('error.html')

    wrap.__name__ = my_function.__name__
    return wrap


def get_next_request_number(Short, Detail):
    """
        :param obj: record of the max request number
    """
    short_request_number = Short.query.order_by(
        Short.request_number.desc()).limit(1).all()
    detail_request_number = Detail.query.order_by(
        Detail.request_number.desc()).limit(1).all()

    if len(short_request_number) == 0 and len(detail_request_number) == 0:
        return 'RZ101'
    else:
        short_num = int(short_request_number[0].request_number[2:]) if len(
            short_request_number) != 0 else 0
        detail_num = int(detail_request_number[0].request_number[2:]) if len(
            detail_request_number) != 0 else 0
        current_max_key_number = max(short_num, detail_num)
        return 'RZ'+str(current_max_key_number+1)


"""
    Utility functions to extract data to be displayed on the website from a JSON file.
"""


def get_data(path='json/data.json'):
    """
        Returns the dictionary representation of the JSON file.
    """
    return json.load(open(path))


def get_segments():
    return get_data()['segments']


def get_retail_services():
    return get_data()['retail-services']


def get_about_us():
    return get_data()['about-us']


def get_main_content():
    """
        Get cherry-picked content from the JSON file for the main page
    """
    data = {}
    data['business'] = get_segments()
    data['service'] = get_retail_services()
    return data


def get_service(id):
    """
        Gets the details of a particular service based on the ID from the JSON file
    """
    return get_data()['retail-services'][id]


def get_business(id):
    """
        Gets the details of a particular business based on the ID from the JSON file
    """
    return get_data()['segments'][id]
