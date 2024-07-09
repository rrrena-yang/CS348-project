HARDCODED_USERNAME="root"
HARDCODED_PASSWORD="MySQL030927"

find query-prod -type f -name '*.sql' | while read -r sql_file; do
    out_file="${sql_file%.sql}.out"
    output=$(mysql -u"$HARDCODED_USERNAME" -p"$HARDCODED_PASSWORD" CS348 < "$sql_file")
    echo "$output" > "$out_file"
done