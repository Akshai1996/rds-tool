#!/bin/bash
if [ -z "$1" ]; then
   echo "REGION environment variable is not set."
   exit 1
else
   echo "Region is: $1"
   export REGION=$1
   python rds.py
fi
