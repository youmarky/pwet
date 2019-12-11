#!/usr/bin/env python3
import yaml
import logging
from lib import mvp  # required for yaml
from lib.mvp import MVP


def load_settings(path):
    with open(path) as f:
        document = f.read()
        document = yaml.load(document)
        logging.debug(document)
    return document


def parse_mvp_list(path):
    with open(path) as f:
        mvp_list = f.read()
        mvp_list = list(yaml.load_all(mvp_list))
        logging.debug(mvp_list)
        logging.debug(", ".join(str([mvp.name, mvp.info]) for mvp in mvp_list))
        mvp_list = _add_mvp_info_to_obj(mvp_list)
    return mvp_list


def _add_mvp_info_to_obj(mvp_list):
    ret_dict = {}
    for yaml_obj in mvp_list:
        # ret_list.append(MVP(yaml_obj))
        ret_dict[yaml_obj.name] = MVP(yaml_obj)
    return ret_dict
