#!/bin/bash
#A script that Displays all HTTP methods the specified url server will accept
curl -X OPTIONS -sI "$1" | sed -n '/Allow/p' | cut -d ":" -f 2 | xargs
