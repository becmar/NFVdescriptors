# Descriptor Generator

##Validate JSON schema
When a NSD/VNFD is generated, please be sure that the file generated is validated correctly with the schema. If not, please update the NSD/VNFD Schema accordingly.

Utility tools:
 - http://jsonschemalint.com (Validate JSON example with the Schema)
 - http://jsonschema.net (Helps with the schema creation)

## Generator installation info

```sh
$ sudo apt-get install python-pip
$ sudo pip install pyyaml
```

## Generate json format descriptors

```sh
$ python descriptors_generator.py
```