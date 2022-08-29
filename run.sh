#!/bin/bash


audio_dir=/home/n2202857e/Documents/Speaker_Embeddings/sample_test_noisy
ext=wav
yaml_file=./yaml/resemblyzer.yml

python scripts/run_batch.py ${audio_dir} ${ext} ${yaml_file}


