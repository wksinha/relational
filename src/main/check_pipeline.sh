#!/bin/bash

test_files=("selection_test_1.in" "selection_test_2.in" "projection_test_1.in" "projection_test_2.in")

for test_file in "${test_files[@]}"; do
    cp "../tests/$test_file" "../main/algebra.in"
    bash run.sh > /dev/null 2> /dev/null

    exit_status=$?
    if [ $exit_status -eq 0 ]; then
        echo "Pipeline passed for $test_file"
    else
        echo "Pipeline failed for $test_file"
    fi
done
