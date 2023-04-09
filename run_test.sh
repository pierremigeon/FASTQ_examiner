#!/bin/bash

if [ $1 -eq 1 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -i
fi

if [ $1 -eq 2 ];
then
	./fastq_examiner.py -f1 ./test_files/head_1 -f2 ./test_files/head_2 -i
fi

if [ $1 -eq 3 ];
then
	./fastq_examiner.py -f1 ./test_files/C1.3.fastq  -f2 ./test_files/C1.4.fastq  -i
fi

if [ $1 -eq 4 ];
then
	./fastq_examiner.py -f1 ./test_files/head_1  -f2 ./test_files/C1.4.fastq  -i
fi

if [ $1 -eq 5 ];
then
	./fastq_examiner.py -f1 ./test_files/singleton_test_f1.fq -f2 ./test_files/singleton_test_f2.fq
fi

if [ $1 -eq 6 ];
then
	./fastq_examiner.py -f1 ./test_files/head_1 -f2 ./test_files/head_2 -i -leaf
fi

#test inputting interleafed file
if [ $1 -eq 7 ];
then
	./fastq_examiner.py -f1 ./test_files/head_leaf_final.fq
fi
