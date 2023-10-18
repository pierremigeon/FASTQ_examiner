#!/bin/bash
####################
##  Old tests...  ##
####################

#input f/r fastq with no flags, as positional arguments, no input files
if [ $1 -eq 0 ];
then 
	echo ./fastq_examiner.py -f -nv
	./fastq_examiner.py -f -nv
fi

#no visual test
#input f/r fastq with no flags, as positional arguments, one input file
if [ $1 -eq 1 ];
then
	echo ./fastq_examiner.py ./test_files/C1.1.fastq -f -nv
	./fastq_examiner.py ./test_files/C1.1.fastq -f -nv
fi

#no visual test
#input f/r fastq with no flags, as positional arguments, two input files
if [ $1 -eq 2 ];
then
	echo ./fastq_examiner.py ./test_files/C1.1.fastq ./test_files/C1.2.fastq -f -nv
	./fastq_examiner.py ./test_files/C1.1.fastq ./test_files/C1.2.fastq -f -nv
fi

#input f/r fastq with no flags, as positional arguments, more than 2 input files:
if [ $1 -eq 3 ];
then
	echo ./fastq_examiner.py ./test_files/C1.1.fastq ./test_files/C1.2.fastq ./test_files/singleton_reads/singleton_test_f1.fq ./test_files/singleton_reads/singleton_test_f1.fq -f -nv
	./fastq_examiner.py ./test_files/C1.1.fastq ./test_files/C1.2.fastq ./test_files/singleton_reads/singleton_test_f1.fq ./test_files/singleton_reads/singleton_test_f1.fq -f -nv
fi

#no visual test


#no visual test
if [ $1 -eq 4 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -f -nv
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -f -nv
fi

#no visual test
if [ $1 -eq 5 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/subsample.C1.1.fastq -f2 ./test_files/subsample.C1.2.fastq -f -nv
	./fastq_examiner.py -f1 ./test_files/subsample.C1.1.fastq -f2 ./test_files/subsample.C1.2.fastq -f -nv
fi

#standard run paired reads with graphical output
if [ $1 -eq 6 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq
fi

#standard run paired reads with graphical output and individual graphs (by file)
if [ $1 -eq 7 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -f 
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -f 
fi

#outputs non-interleaved reads as interleafed to directory ./out/C1
if [ $1 -eq 8 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -leaf
	./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -leaf
fi

#removes singletons and creates seperate singleton files
if [ $1 -eq 9 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/singleton_reads/singleton_test_f1.fq  -f2 test_files/singleton_reads/singleton_test_f2.fq 
	./fastq_examiner.py -f1 ./test_files/singleton_reads/singleton_test_f1.fq  -f2 test_files/singleton_reads/singleton_test_f2.fq 
fi

#output singleton reads seperately, no visual
if [ $1 -eq 10 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/singleton_reads/singleton_test_f1.fq  -f2 test_files/singleton_reads/singleton_test_f2.fq -nv  
	./fastq_examiner.py -f1 ./test_files/singleton_reads/singleton_test_f1.fq  -f2 test_files/singleton_reads/singleton_test_f2.fq -nv  
fi

#test inputting interleafed file
if [ $1 -eq 11 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/leafed_reads/leafed.fq
	./fastq_examiner.py -f1 ./test_files/leafed_reads/leafed.fq
fi

#test inputting interleafed file and output interleafed
if [ $1 -eq 12 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/leafed_reads/leafed.fq -leaf
	./fastq_examiner.py -f1 ./test_files/leafed_reads/leafed.fq -leaf
fi

##########################
##    wrapped tests:    ##
##########################
#Test wrapped files with leafed and unleafed output, for wrap size 37 and 17
#37 lines wrap
if [ $1 -eq 13 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq
fi

if [ $1 -eq 14 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq
fi

#37 lines wrap with leaf output
if [ $1 -eq 15 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq -leaf
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq -leaf
fi

#17 lines wrap
if [ $1 -eq 16 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq
fi

#17 lines wrap with leaf output
if [ $1 -eq 17 ];
then
	echo ./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq -leaf
	./fastq_examiner.py -f1 ./test_files/wrapped_reads/wrap18_F.fq -f2 ./test_files/wrapped_reads/wrap18_R.fq -leaf
fi

###################################
##    leafed singleton tests:    ##
###################################

if [ $1 -eq 18 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_singleton/leafed.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_singleton/leafed.fq -nv
fi

#################################
##    leafed wrapped tests:    ##
#################################

if [ $1 -eq 19 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap15.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap15.fq -nv
fi

if [ $1 -eq 20 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap20.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap20.fq -nv
fi

if [ $1 -eq 21 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap25.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap25.fq -nv
fi

if [ $1 -eq 22 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap30.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped/wrap30.fq -nv
fi

###########################################
##    leafed wrapped singleton tests:    ##
###########################################

if [ $1 -eq 23 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap15.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap15.fq -nv
fi

if [ $1 -eq 24 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap20.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap20.fq -nv
fi

if [ $1 -eq 24 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap25.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap25.fq -nv
fi

if [ $1 -eq 25 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap30.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons/wrap30.fq -nv
fi

#################################################
##    leafed wrapped singleton error tests:    ##
#################################################

if [ $1 -eq 26 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap15.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap15.fq -nv
fi

if [ $1 -eq 27 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap20.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap20.fq -nv
fi

if [ $1 -eq 28 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap25.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap25.fq -nv
fi

if [ $1 -eq 29 ];
then
	echo ./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap30.fq -nv
	./fastq_examiner.py ./test_files/combo_reads/leafed_wrapped_singletons_errors/wrap30.fq -nv
fi
