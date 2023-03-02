#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner QC/Format check module
#@
#############################################@
import re
import os

#############################################
## 	      quality check here
#############################################
#def header(line):
#	header = re.compile('^@')
	

def check_correct_nucleotides(line):
	acceptable = ['A', 'C', 'T', 'G', 'N', 'U', 'a', 't', 'c', 'g', 'n', 'u']
	line = line.rstrip()
	for i in line:
		if i not in acceptable:
			return (False)
	return (True)





#############################################
#  Check to see if the file is wrapped
#############################################
def check_wrapped(file):
	i = 0;
	for line in file:
		if check_correct_nucleotides(line):
			i += 1
		else :
			i = 0	
		if i > 1:
			return (True)
	return (False)

#############################################
#  Check truncation
#############################################
#this function checks to see if there is any sort of truncation:
#makes sure that you have lines with standard format, that qual line == seq line
#and that the sequence is only nucleotides or N.
'''
def check_truncated(file_name):
	file = open(file_name, 'r')
	i = 0;
	line_0 = re.compile('^@.*')
	line_2 = re.compile('^\+')
	for line in file:
		if i == 0 and not line_0.match(line):
			file.close()
			return (True)
		if i == 1:
			if not check_correct_nucleotides(line):
				file.close()
				return (True)
			length_seq = len(line)
		if i == 2 and not line_2.match(line):
			file.close()
			return (True)
		if i == 3:
			if len(line) != length_seq:
				file.close()
				return (True)
			i = -1
		i += 1
	file.close()
	return (False)
'''

def as_read(dict_entry):
	str = ""
	if "header" in dict_entry:
		str += dict_entry["header"]
	if "seq" in dict_entry:
		str += dict_entry["seq"]
		str += "\n"
	if "plus" in dict_entry:
		str += dict_entry["plus"]
	if "qual" in dict_entry:
		str += dict_entry["qual"]
		str += "\n"
	return (str)

def check_truncated(seqs):
	line_0 = re.compile('^@.*')
	line_2 = re.compile('^\+')
	if not os.path.exists("./out"):
		os.makedirs("./out");
	outfile = open("./out/truncated_reads.fastq", 'w')
	removed = 0
	for i in range(len(seqs)):
		for j in range(len(seqs[i])):
			if j > len(seqs[i]) - 1:
				break
			if "header" not in seqs[i][j]:
				removed += 1
				outfile.write(as_read(seqs[i][j]))
				seqs[i].remove(seqs[i][j])
			elif "seq" not in seqs[i][j] or not check_correct_nucleotides(seqs[i][j]["seq"]):
				removed += 1
				outfile.write(as_read(seqs[i][j]))
				seqs[i].remove(seqs[i][j])
			elif "plus" not in seqs[i][j] or not line_2.match(seqs[i][j]["plus"]):
				removed += 1
				outfile.write(as_read(seqs[i][j]))
				seqs[i].remove(seqs[i][j])
			elif "qual" not in seqs[i][j]:
				removed += 1
				outfile.write(as_read(seqs[i][j]))
				seqs[i].remove(seqs[i][j])
			elif not len(seqs[i][j]["seq"]) == len(seqs[i][j]["qual"]):
				removed += 1
				outfile.write(as_read(seqs[i][j]))
				seqs[i].remove(seqs[i][j])
	outfile.close()
	return (removed);

#################################
# Run QC checks:
#################################
def run_QC_checks(files, seqs):
	for file in files:
		the_file = open(file, 'r')
		if check_wrapped(the_file):
			print ("%s included wrapped text. The file will automatically be unwrapped" % file)
		i = check_truncated(seqs)
		if (i):
			print ("%i reads in %s were truncated. %i Truncated entries saved in ./out" % (i, file, i))
		the_file.close()
