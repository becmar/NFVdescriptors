#!/usr/bin/env python
# vnfd_generator.py
# VNFD json file generator

import yaml
import json
from collections import OrderedDict


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

stream = file('vnfd.template.yml', 'r')

vnfd_data = ordered_load(stream, yaml.SafeLoader)
vnfd_json = json.dumps(vnfd_data, indent=2, sort_keys=False)

json_file = open("vnfd.json", "w")
json_file.write(vnfd_json)
json_file.close()