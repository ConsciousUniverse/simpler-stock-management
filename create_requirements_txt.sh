#!/bin/bash
## shellscript to create requirements.txt file from Pipfile.lock
cat Pipfile.lock \
  | grep -B1 '"hashes"\|"version": \|"extras":' \
  | grep -v '"markers": \|"hashes": ' \
  | grep ": {\|version" \
  | sed -e 's/: {$//g' \
  | tr '\n' ',' | tr -s ' ' ' ' \
  | sed -e 's/, "version": "//g;s/", "/ /g;s/"//g;s/,//g' \
  | tr ' ' '\n' \
| grep -v "^$" > requirements.txt