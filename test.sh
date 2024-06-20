find sample-query -type f -name '*.sql' | while read -r sql_file; do
    base_name=$(basename "$sql_file" .sql)
    out_file="${sql_file%.sql}.out"
    output=$(mysql -uroot -p"MySQL030927" CS348_TEST < "$sql_file")
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