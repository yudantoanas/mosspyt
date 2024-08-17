#!/bin/sh

rm -rf clone
rm -rf moss

mkdir clone
mkdir moss

# run main script
python main.py

# run MOSS script
./moss.pl -l python -c "MOSS Results" ./moss/*.py