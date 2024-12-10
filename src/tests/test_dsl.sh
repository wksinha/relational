#!/bin/bash

for input_file in *.in; do
    output_file="${input_file%.in}.out"
    expected_file="${input_file%.in}.expected"
    
    python ../main/RA2SQL.py < $input_file > $output_file
    if diff -qw "$output_file" "$expected_file" > /dev/null; then
        echo "Test passed: $input_file"
        rm $output_file
    else
        echo "Test failed: $input_file"
    fi
done
