#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner format check module
#@
#############################################@
import re
import src.run_QC_checks as rqcc

####################################
# Check basic format correctness
####################################
def third_line(file_name):
	line_3 = re.compile('^\+')
	w = rqcc.check_wrapped(file_name)
	file = open(file_name, 'r')
	for i in range(0, 3):
        	line = file.readline()
	if w:
		while rqcc.check_correct_nucleotides(line):
			line = file.readline()
	file.close()
	return (line_3.match(line))

def legal_seq(file_name):
	file = open(file_name, 'r')
	for i in range(0, 2):
		line = file.readline()
	file.close()
	return (rqcc.check_correct_nucleotides(line))

def starts_at(file_name):
	file = open(file_name)
	header = re.compile('^@')
	line = file.readline()
	file.close()
	return (header.match(line))

#run the above functions, check basic format correct.
def fastq_format_check(files):
	for file in files:
		if not starts_at(file):
			print("First entry in %s doesn't start with a @. %s might not actually be FASTQ format. Exiting." % (os.path.basename(file), os.path.basename(file)))
			sys.exit(0)
		if not legal_seq(file):
			print("The first entry in %s includes non-standard bases (something besides ATCGNU). %s might not actyally be FASTQ format. Exiting." % (os.path.basename(file), os.path.basename(file)))
			sys.exit(0)
		if not third_line(file):
			print("The first entry in %s is missing the '+' line. %s might not actyally be FASTQ format. Exiting." % (os.path.basename(file), os.path.basename(file)))
			sys.exit(0)
