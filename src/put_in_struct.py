#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner put_in_struct module
#@
#############################################@
import re
import src.run_QC_checks as rqcc

def is_error(line):
	if len(line) != 4:
		return True
	if len(line[1]) != len(line[3]):
		return True
	if not re.match('^@', line[0]):
		return True
	if not rqcc.check_correct_nucleotides(line[1]):
		return True
	if not re.match('^\+', line[2]):
		return True
	return False

def check_error(lines, error_lines):
	if len(lines) == 1:
		return
	lines[-1] = [i for i in lines[-1] if i]
	if is_error(lines[-1]):
		error_lines.append(lines[-1])
		lines.pop()

def init_array(line):
	return [line, "", "", "", ]


#
# this handles/detects reads that are:
#	1) incomplete, 
#	2) too many lines (5+)
#	3) lines out of order
#	4) only legal characters used (nucleotides)
#	4) Need to handle nucleotides replacing quality line in future
# And it unwraps lines for both quality and nucleotide, automatically.
# Even if the lines are found out of order
########
#TO DO LIST:
# Next, I would like to run tests on these error detection steps to verify correct function. 
# Then, I will also add some tests for the header region. 
# Then, I will add details of output of incorrect files
# Then, I would like to collect summary statistics and output these to tables.
# It will probably be best to collect all the statistics as the reads are placed in the data structure, then send these summaries to the graphing functions at the end. 
# Next, I would like to detect if headers are inconsistent within the file and between files,
# and I would like to remove singleton reads and place these in a seperate file.
# Paired reads can be interleaved as well. Or they can all be output as is, minus the error reads.
#


#############################################
# Place each file into array of dictionaries
#############################################
def put_in_struct(file_name):
	head = re.compile('^@')
	sep = re.compile('^\+')
	lines = [{"filename" : file_name}]
	error_lines = []
	file = open(file_name, 'r')
	i = -1
	for line in file:
		if not head.match(line) and i == -1:
			if not line.startswith("#"):
				error_lines.append(line)			
		if head.match(line):
			i = 0
			check_error(lines, error_lines)
			lines.append(init_array(line))
		elif sep.match(line):
			i += 1
			lines[-1][i] += line.rstrip()
		else:
			if head.match(lines[-1][i]) or sep.match(lines[-1][i]):
				i += 1
			lines[-1][i] += line.rstrip()
	file.close()
	check_error(lines, error_lines)
	return (lines)
