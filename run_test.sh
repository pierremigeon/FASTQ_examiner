#!/bin/bash
####################
##  Old tests...  ##
####################

if [ $1 -eq 1 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -i -nv
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

#test inputting interleafed file
if [ $1 -eq 8 ];
then
	./fastq_examiner.py -f1 ./test_files/head_leaf_final.fq -leaf
fi

##########################
##  More formal tests:  ##
##########################
#setup to output to the directory the reads are found in 
#Wrapped tests
#37 lines wrap
if [ $1 -eq 9 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap37_F.fq ./test_files/wrapped_reads/wrap37_R.fq
fi

#37 lines wrap with leaf output
if [ $1 -eq 10 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap37_F.fq ./test_files/wrapped_reads/wrap37_R.fq -leaf
fi

#17 lines wrap
if [ $1 -eq 11 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap17_F.fq ./test_files/wrapped_reads/wrap17_R.fq
fi

#17 lines wrap with leaf output
if [ $1 -eq 12 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap17_F.fq ./test_files/wrapped_reads/wrap17_R.fq -leaf
fi
