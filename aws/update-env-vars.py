#!/usr/bin/env python3

###############################################################################
# Created by diggyblock 7/29/23
# chmod the file to make it executable.
# This script takes a json file as an argument, replaced environment varable
#   references with actual values and outputs the result to a file.
# The passed file must contain at least 1 env var reference like $ENV_VAR.
###############################################################################

import os
import json
import sys

# replace function
def update_env_vars(json_str):
    def update_env(match):
        env_variable_name = match.group(1)
        return os.environ.get(env_variable_name, match.group(0))

    import re
    pattern = r"\$([a-zA-Z_][a-zA-Z0-9_]*)"  # Regular expression pattern to match the environment variable placeholder
    return re.sub(pattern, update_env, json_str)

# main function
def main():
    # ensure json file argument was passed
    if len(sys.argv) < 2:
        myself = os.path.basename(__file__)
        print(f"Usage: ./{myself} json_file.json")
        sys.exit(1)

    json_file_path = sys.argv[1]

    try:
        with open(json_file_path, 'r') as json_file:
            json_str = json_file.read()
        
        # ensure passed file contains at least 1 "$"
        if json_str.find("$") < 0:
            print('JSON must contain at least 1 environment variable reference that begins with "$"')
            sys.exit(1)

        updated_json_str = update_env_vars(json_str)

        # write updated string to a file
        output_file = "script_output.json"
        with open(output_file, 'w') as json_file:
            json_file.write(updated_json_str)
        print(f"Updated JSON data written to {output_file}")

    # handle errors
    except FileNotFoundError:
        print("File not found:", json_file_path)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print("Invalid JSON data in the file:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()