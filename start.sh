#!/bin/bash

# Check if arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <python_script> <number_of_times> <csv_file>"
    exit 1
fi

PYTHON_SCRIPT=$1
NUM_RUNS=$(echo "$2" | tr -d '\r')  # Remove hidden carriage return characters
CSV_FILE=$3  # CSV file to store results
# Validate NUM_RUNS as a positive integer
if ! echo "$NUM_RUNS" | grep -qE '^[0-9]+$' || [ "$NUM_RUNS" -le 0 ]; then
    echo "Error: Number of times must be a positive integer!"
    exit 1
fi

echo "Running '$PYTHON_SCRIPT' $NUM_RUNS times concurrently..."

START_TIME=$(date +%s.%N)  # Capture start time

# Run the Python script concurrently the specified number of times
for ((i=1; i<=NUM_RUNS; i++)); do
    echo "test_message_$i" | python "$PYTHON_SCRIPT" &  # Run in the background
done

wait  # Wait for all background jobs to finish

END_TIME=$(date +%s.%N)  # Capture end time

# Calculate total execution time
TOTAL_TIME=$(awk "BEGIN {print $END_TIME - $START_TIME}")
AVERAGE_TIME=$(awk "BEGIN {print $TOTAL_TIME / $NUM_RUNS}")
echo "Total Execution Time: $TOTAL_TIME seconds"
echo "Average Execution Time per script: $AVERAGE_TIME seconds"

echo "$NUM_RUNS,$TOTAL_TIME,$AVERAGE_TIME" >> "$CSV_FILE"

echo "Results stored in $CSV_FILE"