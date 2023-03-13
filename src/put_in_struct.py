#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner put_in_struct module
#@
#############################################@
import re
import os
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

#expand the way you count reads to include header lines that are truncated- in the (somewhat unlikely) case that they lost the first few characters of the line 

def error_out(file_name, error_lines):
	if len(error_lines) == 0:
		return
	read_count = 0
	fname_base = os.path.basename(file_name)
	out_file_name = './out/' + fname_base + '_error_reads.fq'
	out = open(out_file_name, 'w')
	for read in error_lines:
		for line in read:
			newline = 1
			if re.match('^@', line):
				read_count += 1
			if "\n" in line:
				newline = 0
			out.write(line + ("\n" * newline))
	print("%d reads from file %s were determined to be erroneous, removed, and placed in %s" % (read_count, fname_base, out_file_name))

# this handles/detects reads that are:
#	1) incomplete (too few lines), 
#	2) too many lines (>4)
#	3) lines out of order
#	4) only legal nucleotides
#	5) 
# And it unwraps lines for both quality and nucleotide, automatically.
# Even if the lines are found out of order
########
#TO DO LIST:
# Next, I would like to run tests on these error detection steps to verify correct function. 
# Then, I would like to collect summary statistics and output these to tables.
# It will probably be best to collect all the statistics as the reads are placed in the data structure, then send these summaries to the graphing functions at the end. 
# I would like to detect if headers are inconsistent within the file and between files,
# and I would like to remove singleton reads and place these in a seperate file.
# Paired reads can be interleaved as well. Or they can all be output as is, minus the error reads.
#


from difflib import SequenceMatcher

def longest_common_substring(s1: str, s2: str) -> str:
    seq_matcher = SequenceMatcher(isjunk=None, a=s1, b=s2)
    match = seq_matcher.find_longest_match(0, len(s1), 0, len(s2))
    if match.size:
        return s1[match.a : match.a + match.size]
    else:
        return ""

def longest_common_substring_percentage(s1 : str, s2 : str) -> float:
	if min(len(s1), len(s2)) == 0:
		return 0
	return len(longest_common_substring(s1, s2)) / min(len(s1), len(s2))

def fresh_line(line, i):
	if i >= 0:
		return False
	if not re.match('^@', line):
		if not line.startswith("#"):
			return True

def: is_plus(line, info):
	if not re.match('^\+', line):
		return False
	if len(line) < 0.5 * info[2] or len(line) > 0.5 * info[2]
		return False
	if len(line) > 10 and info[4] > 10:
		if line in info[4] or info[4] in line:
			return True
	if longest_common_substring_percentage(line, info[3]) > 0.50:
		return True
	return False

def is_header(line, info):
	if not re.match('^@', line):
		return False
	if len(line) < 0.5 * info[1] or len(line) > 0.5 * info[1]
		return False
	if len(line) > 10 and info[1] > 10:
		 if line in info[3] or info[3] in line:
			return True
	if longest_common_substring_percentage(line, info[3]) > 0.50:
		return True
	return False

#output warning to apropriate locations, error log files or console
def get_common_string(header, tag):
	average_len = reduce(lambda x, y: x + y, map(len, header)) / len(header)
	substr = ""
	for i in average_len:
		common_letter = max(set(header), key=header[i].count)[i]
		filtered = [ h for h in head if h[i] == common_letter ]
		if (len(filtered) / float(i)) * 100 < 75:
			break
		substr += common_letter
	if len(substr) < 0.3 * average_len:
		print("Warning: %s lines are extremely polymorphic." % \
			("header" if tag == "@" else "separator"))
	return substr

def get_info(file):
	head_len = plus_len = other_len = header = plus = []
	i = 0
	line = file.read()
	while i < 4000 and line := file.read():
		if re.match('^@', line):
			head_len.append(len(line))
			header.append(line)
		elif re.match('^\+', line):
			pluses.append(len(line))
		else
			other.append(len(line))
		i += 1
	head_len = max(set(head_len), key=head_len.count)
	plus_len = max(set(pluses), key=pluses.count)
	other_len = max(set(other), key=other.count)
	header = get_commmon_string(header, "@")
	plus = get_common_string(plus, "+")
	return (other_len, head_len, plus_len, header, plus)

#what happens if a quality line starts with @? Need a more concrete means of checking header
#############################################
# Place each file into array of dictionaries
#############################################
def put_in_struct(file_name):
	lines = [{"filename" : file_name}]
	error_lines = []
	file = open(file_name, 'r')
	i = -1
	info = get_info(file)
	file.seek(0)
	for line in file:
		if fresh_line(line, i):
			error_lines.append(line)
		if is_header(line, info)
			i = 0
			check_error(lines, error_lines)
			lines.append(init_array(line))
		elif is_plus(line, info):
			i += 1
			lines[-1][i] += line.rstrip()
		else:
			if head.match(lines[-1][i]) or sep.match(lines[-1][i]):
				i += 1
			lines[-1][i] += line.rstrip()
	file.close()
	check_error(lines, error_lines)
	error_out(file_name, error_lines)
	return (lines)
