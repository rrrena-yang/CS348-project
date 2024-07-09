HARDCODED_USERNAME="root"
HARDCODED_PASSWORD="MySQL030927"

find query-prod -type f -name '*.sql' | while read -r sql_file; do
    base_name=$(basename "$sql_file" .sql)
    out_file="${sql_file%.sql}.out"
    output=$(mysql -u"$HARDCODED_USERNAME" -p"$HARDCODED_PASSWORD" CS348 < "$sql_file")
    echo "$output" > output.txt
    if ! diff -w -q output.txt "$out_file"; then
    echo "Output mismatch for $sql_file"
    echo "===== Expected Output ($out_file) ====="
    cat "$out_file"
    echo "===== Actual Output ====="
    cat output.txt
    exit 1
    fi
done