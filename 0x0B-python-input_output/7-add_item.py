#!/usr/bin/python3
"""Define a function that LOad, add, and save a cmd line argument into a file
   through use of  list appending operation
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


size = len(sys.argv)
i = 1;
with open("add_item.json", "a", encoding="utf-8") as f:
    offset = f.seek(0, 2)
    if not offset:
        cmd_list = []
    else:
        cmd_list = load_from_json_file("add_item.json")
while (i < size):
    cmd_list.append(sys.argv[i])
    i += 1
save_to_json_file(cmd_list, "add_item.json")
