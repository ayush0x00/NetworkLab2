#!/bin/sh

loops=(1000 10000 100000 1000000 10000000 100000000 1000000000)
OUTPUT='./script.txt'

for i in "${loops[@]}"
do
    RES=$(time python3 cpuhog.py ${i})
    echo ${RES} >> ${OUTPUT}
done