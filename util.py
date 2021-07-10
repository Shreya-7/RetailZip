import json
import traceback
from flask import render_template, jsonify, session

# miscellaneous error decorator


def misc_error(my_function):
    def wrap(*args, **kwargs):
        try:
            return my_function(*args, **kwargs)
        except:
            print(traceback.print_exc())
            return render_template('error.html')

    wrap.__name__ = my_function.__name__
    return wrap


def remove_field(obj, fields):

    new_obj = []
    for item in obj:
        for field in fields:
            item.pop(field)
        new_obj.append(item)
    return new_obj


def get_data(path='json/data.json'):
    """
        Returns the dictionary representation of the JSON file.
    """
    return json.load(open(path))


def get_next_request_number(obj: dict):

    if len(obj) == 0:
        return 'RZ101'
    else:
        current_max_key_number = int(obj[0].request_number[2:])
        return 'RZ'+str(current_max_key_number+1)


"""
    Utility functions to extract data to be displayed on the website froma JSON file.
"""


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
    data['business'] = {i: get_business(i) for i in ['B9', 'B2', 'B8', 'B4']}
    data['service'] = {i: get_service(
        i) for i in ['S1', 'S19', 'S8', 'S17', 'S2', 'S14', 'S10', 'S20']}
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
