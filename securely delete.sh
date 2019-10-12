#!/bin/bash

ecco "Insert the name of the file to securely delete"
read file

shred -fuvz "$file"
