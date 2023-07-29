#!/bin/bash
####################
##  Old tests...  ##
####################

#no visual test
if [ $1 -eq 1 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -f -nv
fi

#no visual test
if [ $1 -eq 2 ];
then 
	./fastq_examiner.py -f1 ./test_files/subsample.C1.1.fastq -f2 ./test_files/subsample.C1.2.fastq -f -nv
fi

#standard run paired reads with graphical output
if [ $1 -eq 3 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq
fi

#standard run paired reads with graphical output and individual graphs (by file)
if [ $1 -eq 4 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -f 
fi

#outputs non-interleaved reads as interleafed to directory ./out/C1
if [ $1 -eq 5 ];
then 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -leaf
fi

#removes singletons and creates seperate singleton files
if [ $1 -eq 6 ];
then
	./fastq_examiner.py -f1 ./test_files/singleton_reads/singleton_test_f1.fq  -f2 test_files/singleton_reads/singleton_test_f2.fq 
fi

#output singleton reads seperately, no visual
if [ $1 -eq 7 ];
then
	./fastq_examiner.py -f1 ./test_files/singleton_reads/singleton_test_f1.fq  -f2 test_files/singleton_reads/singleton_test_f2.fq -nv  
fi

#test inputting interleafed file
if [ $1 -eq 8 ];
then
	./fastq_examiner.py -f1 ./test_files/leafed_reads/leafed.fq
fi

#test inputting interleafed file and output interleafed
if [ $1 -eq 9 ];
then
	./fastq_examiner.py -f1 ./test_files/leafed_reads/leafed.fq -leaf
fi

##########################
##    wrapped tests:    ##
##########################
#Test wrapped files with leafed and unleafed output, for wrap size 37 and 17
#37 lines wrap
if [ $1 -eq 10 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap37_F.fq -f2 ./test_files/wrapped_reads/wrap37_R.fq
fi

#37 lines wrap with leaf output
if [ $1 -eq 11 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap37_F.fq -f2 ./test_files/wrapped_reads/wrap37_R.fq -leaf
fi

#17 lines wrap
if [ $1 -eq 12 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap17_F.fq -f2 ./test_files/wrapped_reads/wrap17_R.fq
fi

#17 lines wrap with leaf output
if [ $1 -eq 13 ];
then
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap17_F.fq -f2 ./test_files/wrapped_reads/wrap17_R.fq -leaf
fi
