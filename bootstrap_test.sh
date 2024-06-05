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
read -p "This action will reset the database CS348_TEST. Are you sure? [y/n]: " confirm
confirm=${confirm,,}  # tolower
if [[ "$confirm" != "y" && "$confirm" != "" ]]; then
    echo "Aborted!"
    exit 1
fi

# Export password as an environment variable
export MYSQL_PWD="$password"

# Run the SQL script from bootstrap.sql
mysql -u "$username" <<EOF
$(cat bootstrap_test.sql)
EOF

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Database CS348_TEST has been reset successfully."
else
    echo "Failed to reset the database CS348_TEST."
    unset MYSQL_PWD
    exit 1
fi

# View tables in the database
mysql -u"$username" -e "USE CS348_TEST; SHOW TABLES;"

# Unset the password environment variable
unset MYSQL_PWD