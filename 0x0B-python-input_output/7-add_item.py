#!/usr/bin/python3
"""
Module for creating an Object from a “JSON file”:
"""
import json
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Reads command line arguments and saves them in json file.
    """
    try:
        filename = "add_item.json"
        try:
            # loading list from json file
            items = load_from_json_file(filename)
        except Exception:
            items = []
        for arg in sys.argv[1:]:
            items.append(arg)
        save_to_json_file(items, filename)
    except json.decoder.JSONDecodeError:
        pass


if __name__ == "__main__":
    main()
