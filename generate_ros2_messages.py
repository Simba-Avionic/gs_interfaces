import os
import sys
import json
import argparse
import xml.etree.ElementTree as ET

CONFIG_PATH = "../config.json"
SIMBA_XML_PATH = "../mavlink/simba_mavlink/simba.xml"
NEW_LINE = "\n"

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils
from utils.paths import CONFIG_JSON_PATH, SIMBA_XML_PATH


def create_msg_files():
    # Read config.json
    with open(CONFIG_JSON_PATH, 'r') as f:
        config = json.load(f)

    message_files_names = []

    for msg_def in config['msg_defs']:
        msg_type = msg_def['msg_type']
        msg_fields = msg_def['msg_fields']
        msg_definition = f"# {msg_type} message"
        msg_definition += (f"{NEW_LINE}# ---{NEW_LINE}")
        for field in msg_fields:
            msg_definition += (f"{field['type']} {field['val_name']} {NEW_LINE}")

        # Write message definition to .msg file
        msg_file_path = f'msg/{msg_type}.msg'
        with open(msg_file_path, 'w') as msg_file:
            msg_file.write(msg_definition)

        print(f'Message definition written to {msg_file_path}')
        message_files_names.append(f'{msg_type}.msg')

    # Process config data
    for topic in config['topics']:
        msg_type = topic['msg_type']
        msg_fields = topic['msg_fields']
        msg_definition = f"# {msg_type} message"
        msg_definition += (f"{NEW_LINE}# ---{NEW_LINE}")
        for field in msg_fields:
            msg_definition += (f"{field['type']} {field['val_name']} {NEW_LINE}")

        # Write message definition to .msg file
        msg_file_path = f'msg/{msg_type}.msg'
        with open(msg_file_path, 'w') as msg_file:
            msg_file.write(msg_definition)

        print(f'Message definition written to {msg_file_path}')
        message_files_names.append(f'{msg_type}.msg')

    return message_files_names


def create_msg_files_from_xml():
    tree = ET.parse(SIMBA_XML_PATH)
    root = tree.getroot()

    message_files_names = []

    # Process XML data
    for message in root.findall('messages/message'):
        msg_type = utils.convert_message_name(message.get('name'))
        msg_definition = f"# {msg_type} message"
        msg_definition += (f"{NEW_LINE}# ---{NEW_LINE}")
        msg_definition += f"std_msgs/Header header{NEW_LINE}"
        for field in message.findall('field'):
            field_type = utils.get_type_mapping(field.get('type'))
            field_name = field.get('name')
            msg_definition += (f"{field_type} {field_name} {NEW_LINE}")

        # Write message definition to .msg file
        msg_file_path = f'msg/{msg_type}.msg'
        with open(msg_file_path, 'w') as msg_file:
            msg_file.write(msg_definition)

        print(f'Message definition written to {msg_file_path}')
        message_files_names.append(f'{msg_type}.msg')

    return message_files_names


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Generate ROS message files from JSON and/or XML sources.')
    parser.add_argument('--json', action='store_true',
                        help='Generate messages from config.json')
    parser.add_argument('--xml', action='store_true',
                        help='Generate messages from simba.xml')
    parser.add_argument('--all', action='store_true',
                        help='Generate messages from both sources')
    
    args = parser.parse_args()

    os.makedirs('msg', exist_ok=True)

    if not (args.json or args.xml or args.all):
        args.json = True

    if args.json or args.all:
        print("Generating ROS messages from JSON...")
        _ = create_msg_files()
        
    if args.xml or args.all:
        print("Generating ROS messages from XML...")
        _ = create_msg_files_from_xml()