"""
Short Python example showing how it is possible to use the schema to validate 
a JSON file against a schema

Requires one package not in the standard library (jschon).
"""
import os
import json
from jschon import create_catalog, JSON, JSONSchema

schema_filename = os.path.join(
    '.',
    'draft_schema_and_networks',
    'draft_bmopf_schema.json'
)

# the two examples to choose from for now
examples_dir = os.path.join('.','draft_schema_and_networks','network_examples',)

# choose the schema type
catalog = create_catalog('2020-12')
with open(schema_filename) as file:
    bmopf_schema = JSONSchema(json.loads(file.read()))

for file_name in os.listdir(examples_dir):
    if file_name[-4:]=='json':
        with open(os.path.join(examples_dir, file_name)) as file:
            instance = JSON(json.loads(file.read()))

        result = bmopf_schema.evaluate(instance)
        assert(result.output('basic')['valid'])

print(f'All networks conform to the json schema from the directory:\n\t{examples_dir}')
