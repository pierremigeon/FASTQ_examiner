#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner put_in_struct module
#@
#############################################@
import re
import src.run_QC_checks as rqcc

#############################################
# Place each file into array of dictionaries
#############################################
def put_in_struct(file_name):
	header = rqcc.get_header(file_name)
	header = re.compile(header)
	non_seq = re.compile('^\+')
	lines = []
	j = -1
	file = open(file_name, 'r')
	for line in file:
		if header.match(line):
			lines.append({"header" : line})
			if j == -1:
				lines[0]["filename"] = file_name
			i = 1
			j += 1
		if i == 1 and rqcc.check_correct_nucleotides(line):
			if "seq" in lines[j]:
				lines[j]["seq"] += line.rstrip()
			else:
				lines[j]["seq"] = line.rstrip()
		if i == 2:
			if "qual" in lines[j]:
				lines[j]["qual"] += line.rstrip()
			else:
				lines[j]["qual"] = line.rstrip()
		if i == 1 and non_seq.match(line):
			lines[j]["plus"] = line;
			i += 1
	file.close()
	return (lines)

