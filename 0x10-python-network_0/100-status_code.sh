#!/bin/bash
# Capture the status-code of a response only
curl -s -o /dev/null -w "%{http_code}" "$1"
