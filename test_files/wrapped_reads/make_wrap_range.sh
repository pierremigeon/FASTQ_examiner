#!/bin/bash 

for ((i = 1; i <= $1; i++)) do
	perl make_wrap.pl *fastq $i
done;
