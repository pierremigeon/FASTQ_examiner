#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner put_in_struct module
#@
#############################################@
import re
import src.run_QC_checks as rqcc

def is_error(line):
	if len(line) == 0:
		return False
	if len(line) != 4:
		return True
	# check correct header
	#if 
	# check correct Seq line
	#if
	# check correct + line
	#if 
	# check correct quality line


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
# this should handle/detect reads that are incomplete, 
# reads that have too many lines,
# reads that have lines out of order, 
# and also unwrap lines for both quality and nucleotide, 
# even if the unwrapped lines are found out of order.
#
# the check error and is_error functions check that only legal
# characters (nucleotide and quality) are used. 
# 
# Next, I would like to detect if headers are inconsistent within the file and between files,
# and I would like to remove singleton reads and place these in a seperate file.
# Paired reads can be interleaved as well. Or they can all be output as is, minus the error reads.
# Need to take user input for these details.
#


#############################################
# Place each file into array of dictionaries
#############################################
def put_in_struct(file_name):
	#head = rqcc.get_header(file_name)
	head = re.compile('^@')
	sep = re.compile('^\+')
	lines = [{"filename" : file_name}]
	error_lines = []
	i = -1
	file = open(file_name, 'r')
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
