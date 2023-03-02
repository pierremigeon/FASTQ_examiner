#!/bin/bash

if [ $1 -eq 1 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -i
fi

if [ $1 -eq 2 ];
then
	./fastq_examiner.py -f1 ./test_files/head_1 -f2 ./test_files/head_2 -i
fi


