#!/bin/bash
# POST method with a JSON file as data content to the server
curl -sH Content-Type: application/json -d "$(cat $2)" "$1"
