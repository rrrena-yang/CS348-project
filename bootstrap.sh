#!/bin/bash

# Hardcoded username and password (leave empty for prompting)
HARDCODED_USERNAME=""
HARDCODED_PASSWORD=""

# Prompt for MySQL username if not hardcoded
if [ -z "$HARDCODED_USERNAME" ]; then
    read -p "Enter MySQL username: " username
else
    username="$HARDCODED_USERNAME"
fi

# Prompt for MySQL password if not hardcoded
if [ -z "$HARDCODED_PASSWORD" ]; then
    read -s -p "Enter MySQL password: " password
    echo
else
    password="$HARDCODED_PASSWORD"
fi

# Confirm resetting the database
read -p "This action will reset
