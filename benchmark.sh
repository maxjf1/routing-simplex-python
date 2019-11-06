#!/bin/bash

# Roda para todas instâncias

rm -rf ./logs/*.log

my_array=(
    c101
    c102
    c103
    c104
    c105
    c106
    c107
    c108
    c109
    c201
    c202
    c203
    c204
    c205
    c206
    c207
    c208
    r101
    r102
    r103
    r104
    r105
    r106
    r107
    r108
    r109
    r110
    r111
    r112
    r201
    r202
    r203
    r204
    r205
    r206
    r207
    r208
    r209
    r210
    r211
    rc101
    rc102
    rc103
    rc104
    rc105
    rc106
    rc107
    rc108
    rc201
    rc202
    rc203
    rc204
    rc205
    rc206
    rc207
    rc208
)

for i in "${my_array[@]}"; do
    (gurobi.sh main.py ./models/$i.txt || echo "FAIL!") 1>> ./logs/$i.log;
done