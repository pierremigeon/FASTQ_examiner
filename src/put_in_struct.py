#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner put_in_struct module
#@
#############################################@
import re
import os
import src.run_QC_checks as rqcc
from functools import reduce 
#import pdb; pdb.set_trace()

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

def handle_error(lines, error_lines):
	if len(lines) == 1:
		return
	lines[-1] = [i for i in lines[-1] if i]
	if is_error(lines[-1]):
		error_lines.append(lines[-1])
		lines.pop()
	else:
		lines[0]["headers"][lines[-1][0]] = len(lines) - 2

def init_array(line):
	return [line.rstrip(), "", "", "", ]

def error_out(file_name, error_lines):
	if len(error_lines) == 0:
		return
	read_count = 0 
	fname_base = os.path.splitext(os.path.basename(file_name))[0]
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
# And it unwraps lines for both quality and nucleotide, automatically.
# Even if the lines are found out of order
########
#TO DO LIST:
# I would like to run tests on these error detection steps to verify correct function. 
# I would like to collect summary statistics and output these to tables, collecting data as the reads are read.
# I would like to detect if headers are inconsistent within the file and between files,
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

def is_plus(line, info):
	if not re.match('^\+', line):
		return False
	if len(line) < 0.5 * info[2] or len(line) > 1.5 * info[2]:
		return False
	if len(line) > 10 and info[2] > 10:
		if line in info[4] or info[4] in line:
			return True
	if longest_common_substring_percentage(line, info[4]) > 0.50:
		return True
	return False

def is_header(line, info):
	if not re.match('^@', line):
		return False
	if len(line) < 0.5 * info[1] or len(line) > 1.5 * info[1]:
		return False
	if len(line) > 10 and info[1] > 10:
		if line in info[3] or info[3] in line:
			return True
	if longest_common_substring_percentage(line, info[3]) > 0.50:
		return True
	return False

#output warning to apropriate locations, error log files or console
def get_common_string(header, tag):
	average_len = round(reduce(lambda x, y: x + y, map(len, header)) / len(header))
	substr = ""
	zip_list = list(zip(*header))
	for i in range(average_len):
		common_letter = max(set(zip_list[i]), key=zip_list[i].count)
		filtered = [ h for h in header if h[i] == common_letter ]
		if (len(filtered) / float(len(header))) * 100 < 75:
			break
		substr += common_letter
	if len(substr) < 0.25 * average_len:
		print("Warning: %s lines are extremely polymorphic, short consensus obtained." % \
			("header" if tag == "@" else "separator"))
	return substr

def check_leaf_status(leaved):
	return leaved[0] and leaved[1]

def set_values(o_len, h_len, p_len, header, plus, leaved):
	o_len = max(set(o_len), key=o_len.count)
	h_len = max(set(h_len), key=h_len.count)
	p_len = max(set(p_len), key=p_len.count)
	header = get_common_string(header, "@")
	plus = get_common_string(plus, "+")
	leaved = check_leaf_status(leaved)
	return (o_len, h_len, p_len, header, plus, leaved)

def get_info(file):
	o_len, h_len, p_len, header, plus = [], [], [], [], []
	i = 0
	leaved = [False, False]
	line = file.readline()
	while i < 2000 and (line := file.readline()):
		if re.match('^@', line):
			h_len.append(len(line))
			header.append(line)
			leaved[0] = line[-2:] == "/1"
			leaved[1] = line[-2:] == "/2"
		elif re.match('^\+', line):
			p_len.append(len(line))
			plus.append(line)
		else:
			o_len.append(len(line))
		i += 1
	return (set_values(o_len, h_len, p_len, header, plus, leaved))

def check_type(line):
	if rqcc.check_correct_nucleotides(line):
		return "Seq"
	return "Qual"

def line_same_type(type, old_line, new_line):
	if type != "":
		return False
	type_1 = check_type(old_line)
	type_2 = check_type(new_line)
	if type_1 == type_2:
		return True
	return False

def get_lines_dictionary():
	return [{"filename" : file_name, "headers" : {}, \
		"head" : info[3], leaved : False}]

#############################################
# Place each file into array of dictionaries
#############################################
def put_in_struct(file_name):
	file = open(file_name, 'r')
	info = get_info(file)
	lines = get_lines_dictionary()
	error_lines = []
	i = -1
	file.seek(0)
	last_type = ""


#Next: once you determine the file is interleafed, you want to add all the /2 files at the end of the array and all the /1 files sequencially, so track the head of the forward and put the reads there. Then in the main file, you split this into two distinct files in the seqs array.

	for line in file:
		if fresh_line(line, i):
			error_lines.append(line)
		if is_header(line, info):
			i = 0
			handle_error(lines, error_lines)
			lines.append(init_array(line))
			last_type = "Header"
		elif is_plus(line, info):
			i += 1
			lines[-1][i] += line.rstrip()
			last_type = "Plus"
		else:
			if not line_same_type(last_type, lines[-1][i], line):
				i += 1
			lines[-1][i] += line.rstrip()
			last_type = ""
	file.close()
	handle_error(lines, error_lines)
	error_out(file_name, error_lines)
	return (lines)
