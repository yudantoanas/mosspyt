#!/bin/sh

# run main script
python main.py

# run MOSS script
./moss.pl -l python -c "MOSS Results" ./outputs/*.py 