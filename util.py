import json

path = 'data.json'


def get_data():
    return json.load(open(path))


def get_segments():
    return get_data()['segments']


def get_retail_services():
    return get_data()['retail-services']


def get_associate_services():
    return get_data()['associate-services']


def get_main_content():
    data = {}
    data['business'] = {i: get_business(i) for i in ['B9', 'B2', 'B8', 'B4']}
    data['service'] = {i: get_service(i) for i in ['S1', 'S19', 'S8', 'S17']}
    data['associate'] = {i: get_service(i) for i in ['A2', 'A4', 'A1']}
    return data


def get_service(id):

    key = ''
    if 'A' in id:
        key = 'associate-services'
    else:
        key = 'retail-services'

    return get_data()[key][id]


def get_business(id):
    return get_data()['segments'][id]
