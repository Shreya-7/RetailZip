# This file deals with all functions related to data access, storage and manipulation

import json
import traceback


def get_next_request_number(db):
    """
        :param obj: record of the max request number
    """
    request = db.find({}).sort("request_number", -1).limit(1)

    if request is None:
        return 'RZ101'
    else:
        current_request_number = int(request[0]["request_number"][2:])
        return 'RZ'+str(current_request_number+1)


def domain_mapper(source, fields=[]):
    dest = {}
    for field in fields:
        field = field.lower()
        if field in source.keys():
            dest[field] = source[field]
    return dest


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
