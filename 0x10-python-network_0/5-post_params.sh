#!/bin/bash
# A Bash script that takes in a URL, set Method to POST, and display body of the response
curl -sX POST -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"
