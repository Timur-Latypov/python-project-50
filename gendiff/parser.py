import yaml
import json


def parse(data, data_format):
    if data_format == '.json':
        return json.load(data)
    elif data_format in ('.yml', '.yaml'):
        return yaml.load(data, Loader=yaml.CLoader)
