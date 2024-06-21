#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# Hardcoded username and password (leave empty for prompting)
HARDCODED_USERNAME="root"
HARDCODED_PASSWORD="MySQL030927"

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
read -p "This action will reset the database CS348_TEST. Are you sure? [y/n]: " confirm
confirm=${confirm,,}  # tolower
if [[ "$confirm" != "y" && "$confirm" != "" ]]; then
    echo "Aborted!"
    exit 1
fi

# Export password as an environment variable
export MYSQL_PWD="$password"

# Run the SQL script create_table.sql located relative to the script
mysql -u "$username" < "$SCRIPT_DIR/create_table.sql"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "create_table.sql executed successfully."
else
    echo "Failed to execute create_table.sql."
    unset MYSQL_PWD
    exit 1
fi

# Run the SQL script bootstrap_test.sql located relative to the script
mysql -u "$username" CS348_TEST < "$SCRIPT_DIR/bootstrap_test.sql"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "bootstrap_test.sql executed successfully."
else
    echo "Failed to execute bootstrap_test.sql."
    unset MYSQL_PWD
    exit 1
fi

echo "Database CS348_TEST has been reset successfully."

# View tables in the database
mysql -u "$username" -e "USE CS348_TEST; SHOW TABLES;"

# Unset the password environment variable
unset MYSQL_PWD
