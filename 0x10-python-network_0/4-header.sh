#!/bin/bash
# Send additional Header to a server with curl
curl -s -X GET -H "X-School-User-Id: 98" "$1"
