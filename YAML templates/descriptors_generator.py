#!/usr/bin/env python
# descriptors_generator.py
# VNFD json file generator

import yaml
import json
import re
import os

from yaml.parser import ParserError
from yaml.scanner import ScannerError

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

print 'Scanning "%s" directory for YAML templates (*.template.yml) ...' % os.path.dirname(os.path.realpath(__file__))

yml_template_files = [f for f in os.listdir('.') if re.match(r'.*template.yml', f)]

print '%s YAML templates found.\n' % len(yml_template_files)

for yml_template in yml_template_files:
    print 'generating %s file...' % yml_template
    try:
        stream = file(yml_template, 'r')

        data = ordered_load(stream, yaml.SafeLoader)
        jsondata = json.dumps(data, indent=2, sort_keys=False)

        new_filename = yml_template.replace('template.yml', 'json')
        json_file = open(new_filename, "w")
        json_file.write(jsondata)
        json_file.close()

        print '- %s file generated.' % new_filename
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ParserError as e:
        print "Parse error({0}): {1}".format(e.message, e.problem)
    except ScannerError as e:
        print "Scanner error, {0}".format(e.problem)
