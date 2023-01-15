#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner QC check module
#@
#############################################@
import re
import os

#############################################
## 	      quality check here
#############################################
def check_correct_nucleotides(line):
	acceptable = ['A', 'C', 'T', 'G', 'N', 'U', 'a', 't', 'c', 'g', 'n', 'u']
	line = line.rstrip()
	for i in line:
		if i not in acceptable:
			return (False)
	return (True)

'''
 The following is only relevant in some rare 
 cases (Sanger style fastq, for instance)
 But will still be useful to detect in such 
 a case. Only checks sequence lines assuming
 that these are the only things that are 
 wrapped. Wrapped seq ID lines will throw a
 trunctation error.
'''
#############################################
#  Unwrap the files 
#############################################
#cannot handle early/first read truncation
def get_header(file_name):
	header = re.compile('^@')
	plus = re.compile('^\+')
	file = open(file_name, 'r')
	first_line = file.readline()
	if len(first_line) < 2:
		print("Minimal information stored in the header line... Possible bugs ahead. You may want to reformat headerlines.")
	seq_line = file.readline()
	x = 0
	if len(seq_line) == len(first_line):
		x = 1
	i = 2
	last_line = seq_line
	for line in file:
		if header.match(line) and not plus.match(last_line):
			if len(line) != len(seq_line) or x:
				if len(os.path.commonprefix([first_line, line])) > 1: 
					first_line = os.path.commonprefix([first_line, line])
		last_line = line
		i += 1
	file.close()
	return (first_line)

'''
def unwrap(file_name):
	header = get_header(file_name)
	line_2 = re.compile('^\+|^\+header')
	header = re.compile(header)
	file = open(file_name, 'r')
	out_path = "./out/" + os.path.splitext(os.path.basename(file_name))[0] + ".unwrapped.fastq"
	if not os.path.exists(out_path):
		os.makedirs(out_path)	 
	out = open(out_path, 'w')
	growing_line = ""
	i = 0
	for line in file:
		if header.match(line):
			if i == 0:
				i += 1
				out.write(line)
			else:
				 out.write("\n" + line)
		elif line_2.match(line):
			out.write("\n" + line)
		else :
			out.write(line.rstrip())
	out.write("\n")
	file.close()
	out.close()
'''

#############################################
#  Check to see if the file is wrapped
#############################################
def check_wrapped(file_name):
	file = open(file_name, 'r')
	i = 0;
	for line in file:
		if check_correct_nucleotides(line):
			i += 1
		else :
			i = 0	
		if i > 1:
			file.close()
			return (True)
	file.close()
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
		if check_wrapped(file):
			print ("%s included wrapped text. The file will automatically be unwrapped" % file)
		i = check_truncated(seqs)
		if (i):
			print ("%i reads in %s were truncated. %i Truncated entries saved in ./out" % (i, file, i))
