#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner format check module
#@
#############################################@
import re
import os
import sys
import src.run_QC_checks as rqcc

####################################
# Check basic format correctness
####################################
def third_line(file):
	line_3 = re.compile('^\+')
	line = file.readline()
	w = rqcc.check_wrapped(file)
	if w:
		while rqcc.check_correct_nucleotides(line):
			line = file.readline()
	print(line)
	return (line_3.match(line))

def legal_seq(file):
	line = file.readline()
	return (rqcc.check_correct_nucleotides(line))

def starts_at(file):
	header = re.compile('^@')
	line = file.readline()
	return (header.match(line))

#run the above functions, check basic format correct.
def fastq_format_check(files):
	for file in files:
		the_file = open(file, 'r')
		if not starts_at(the_file):
			print("First entry in %s doesn't start with a @. %s might not actually be FASTQ format. Exiting." % (os.path.basename(file), os.path.basename(file)))
			sys.exit(0)
		if not legal_seq(the_file):
			print("The first entry in %s includes non-standard bases (something besides ATCGNU). %s might not actyally be FASTQ format. Exiting." % (os.path.basename(file), os.path.basename(file)))
			sys.exit(0)
		if not third_line(the_file):
			print("The first entry in %s is missing the '+' line. %s might not actyally be FASTQ format. Exiting." % (os.path.basename(file), os.path.basename(file)))
			sys.exit(0)
		the_file.close()
