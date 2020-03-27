import argparse
import json

def format_table_value(value, size):
    if type(value):
        value = str(value)

    return value[: size - 1] + '\u2026' if len(value) > size else value
    
parser = argparse.ArgumentParser(description='''
    Merges postman artifacts.\n
    The order in which the files are listed, determines the priority of the merge.\n
    This means that a subsequent file will override any keys by default.''')
parser.add_argument('-e', '--environment', action="store_true", default=True)
parser.add_argument('-f', '--files', nargs='+', help='<Required> Files to merge', required=True)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-p', help='Print options', action='store_true', dest='print', default=False)

args = parser.parse_args()

if args.print:
    print(f'::: Options provided: {args}')

for path in args.files:
    # TODO: validate file exist
    with open(path) as f:
        # TODO: validate file is JSON compliant
        data = json.load(f)
        # TODO: validate there is an id (JSON schema)
        print(data['id'])
        print("{:<30} {:<30} {:<30}".format('key', 'value', 'enabled'))
        print(80 * "=")
        # TODO: validate there is a values attribute (JSON schema)
        for x in data['values']:
            print("{:<30} {:<30} {:<30}".format(
                format_table_value(x['key'], 30),
                format_table_value(x['value'], 30),
                format_table_value(x['enabled'], 30)))

