import os
import json

CONFIG_PATH = "../server/config.json"
# CMAKE_PATH = "CMakeLists.txt"
NEW_LINE = "\n"

def create_msg_files():
    # Read config.json
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)

    message_files_names = []

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


if __name__ == "__main__":
    msg_names = create_msg_files()