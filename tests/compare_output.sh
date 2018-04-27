#!/bin/bash

# directory with results
DIR=out

#make array of expected files
declare -a arrExp
for file in $DIR/expected_test_*.csv
do
	arrExp=(${arrExp[@]} "$file")
done

#make array of results from tests
declare -a arrRes
for result in $DIR/result_*.csv
do
	arrRes=(${arrRes[@]} "$result")
done

# compare expected to results
for i in ${!arrExp[*]};
do
	if diff ${arrExp[$i]} ${arrRes[$i]}; then : ; else echo FAILED; exit 1; fi
done

echo PASSED
exit 0
