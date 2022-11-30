#! /usr/bin/bash

scp rivanna:/scratch/dub5nq/mlcommons/benchmarks/cloudmask/target/* .

python graphMaker.py

mv *.log graphs
