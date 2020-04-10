#!/bin/bash

echo "Insert the name of the file to securely delete"
read file

shred -n 10 -fuvz "$file"

echo
echo "DONE"