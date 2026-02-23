#!/bin/bash

echo "Generating files..."
for i in {1..10}; do
    filename="file_$i.txt"
    echo "This is file number $i" > "$filename"
    echo "Generated $filename"
done
echo "File generation complete."