import os
import sys
import json
import xml.etree.ElementTree as ET

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
    os.makedirs('msg', exist_ok=True)
    msg_names = create_msg_files()
    msg_names_xml = create_msg_files_from_xml()