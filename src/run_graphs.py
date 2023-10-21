#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner quality graphs module
#@
#############################################@
import numpy as np
import matplotlib.pyplot as plt
import os

#############################################
## %N Basecalls / Base Graph Functions
#############################################
def plot_total_ns(N_count, file_name):
	max_length = N_count.argmin()
	plt.plot(100 * (N_count[0:max_length] / N_count[750:max_length + 750]), color = 'mediumblue') #, linestyle='dashed')
	plt.xlabel("Position in Read")
	plt.ylabel("Percent N")
	if file_name:
		plt.title("%%N by length of read for %s" % file_name)
	else:
		plt.title("%N by length of read cumulative for all files")
	plt.minorticks_on()
	plt.grid(visible=True, which='major', color='grey', linewidth=0.2)
	plt.grid(visible=True, which='minor', color='grey', linewidth=0.2)
	plt.show()

#This is to summarize the bases where Ns were found.
def summarize_ns(file, plot_number):
	N_count = np.zeros((1500,), dtype=float)
	max_length = 0;
	i = 0
	file_name = file[0]['filename']
	for read in file[1:len(file)]:
		j = 0
		for char in read[1]:
			N_count[j + 750] += 1
			if char == "N":
				N_count[j] += 1
			j += 1
		if j > max_length:
			max_length = j
	if plot_number:
		plot_ns(N_count, os.path.basename(file_name))
	return(N_count)

##########################################################
#  Number / Total Read Length Graph Functions
##########################################################
def plot_number_of_x_length(lens, max_len, file_name):
	plt.xlabel("Length of Read")
	plt.ylabel("Number of Reads")
	plt.plot(lens[0:max_len + 2], color = 'mediumblue') #, linestyle='dash_dot')
	plt.title("Read Length Distribution for %s" % os.path.basename(file_name))
	plt.minorticks_on()
	plt.grid(visible=True, which='major', color='grey', linewidth=0.2)
	plt.grid(visible=True, which='minor', color='grey', linewidth=0.2)
	plt.show()

#This function plots the length distribution for the reads.
def number_of_x_length(seqs, file_plots):
	t_lens = np.zeros((750,), dtype=int)
	max_len = 0;
	for i in range(len(seqs)):
		lens = np.zeros((750,), dtype=int)
		for j in range(1, len(seqs[i])):
			length = len(seqs[i][j][1])
			lens[length] += 1
			if length > max_len:
				max_len = length
		t_lens += lens
		if (file_plots):
			plot_number_of_x_length(lens, max_len, seqs[i][0]["filename"])
	plot_number_of_x_length(t_lens, max_len, "All Files")

######################################
#  %GC / Base Graph Functions
######################################
def polish_arrays(nucleotides, max_len):
	for base_1 in nucleotides:
		if max_len < len(nucleotides[base_1]):
			max_len = len(nucleotides[base_1])
	for base_2 in nucleotides:
		while len(nucleotides[base_2]) < max_len:
			nucleotides[base_2] = np.append(nucleotides[base_2], 0)

def trim_array_ends(array):
	while [array[i][-1] for i in array] == [0,0,0,0,0]:
		for i, x in enumerate(array):
			array[x] = array[x][:-1]			

def plot_percent_gc(nucleotides, max_len, file_name):
	polish_arrays(nucleotides, max_len)
	sums = sum(nucleotides[i] for i in nucleotides)
	sums[sums == 0] = 1
	for letter in nucleotides:
		nucleotides[letter] /= sums
	trim_array_ends(nucleotides)
	plt.xlabel("Position in Read")
	plt.ylabel("Proportion of Base")
	plt.title("Base Composition By Read Position For %s" % os.path.basename(file_name))
	plt.plot(nucleotides["A"][0:max_len], color = 'red')
	plt.plot(nucleotides["T"][0:max_len], color = 'mediumblue')
	plt.plot(nucleotides["C"][0:max_len], color = 'yellow')
	plt.plot(nucleotides["G"][0:max_len], color = 'green')
	plt.legend(["A", "T", "C", "G"])
	plt.minorticks_on()
	plt.grid(visible=True, which='major', color='grey', linewidth=0.2)
	plt.grid(visible=True, which='minor', color='grey', linewidth=0.2)
	plt.show()

def make_nucleotides(length):
	nucleotides = [] 
	nucleotides.append({"A" : np.zeros(length), "T" : np.zeros(length), "C" : np.zeros(length), "G" : np.zeros(length), "N" : np.zeros(length)})
	return nucleotides

#Cannot handle lowercase- convert to all caps and print notification of case change
def percent_gc(seqs, file_plots):
	nucleotides = make_nucleotides(len(seqs[0][1][1]))
	max_len = 0
	for i in (range(len(seqs))):
		nucleotides += make_nucleotides(len(seqs[0][0]))
		for j in (range(1, len(seqs[i]))):
			x = 0
			for letter in seqs[i][j][1]:
				while x >= len(nucleotides[i + 1][letter]):
					nucleotides[i + 1][letter] = np.append(nucleotides[i + 1][letter], 0)
				nucleotides[i + 1][letter][x] += 1
				while x >= len(nucleotides[0][letter]):
					nucleotides[0][letter] = np.append(nucleotides[0][letter], 0)
				nucleotides[0][letter][x] += 1
				x += 1
			if x >= max_len:
				max_len = x
		if file_plots or len(seqs) == 1:
			plot_percent_gc(nucleotides[i + 1], max_len, seqs[i][0]['filename'])
	if (len(nucleotides) > 2):
		plot_percent_gc(nucleotides[0], max_len, "All Files")

######################################
#  Quality/Base Graph Functions
######################################
def plot_count_by_quality(sum, file_name):
	plt.plot(sum[0:], color = 'mediumblue', linewidth=2)
	plt.title("Count of Reads Per Quality Score for %s" % os.path.basename(file_name))
	plt.xlabel("Quality Score")
	plt.ylabel("Number of Reads")
	plt.minorticks_on()
	plt.grid(visible=True, which='major', color='grey', linewidth=0.2)
	plt.grid(visible=True, which='minor', color='grey', linewidth=0.2)
	plt.show()

def average_qual(qual_str, encoding):
	length = len(qual_str)
	qual_int = 0
	if encoding == 33:
		base = ord('!')
	else:
		base = ord('@')
	for char in qual_str:
		qual_int += ord(char) - base
	return (int(qual_int / length + 0.5))

def get_encoding(seqs):
	min = '~'
	max = '!'
	for entry in range(1, len(seqs)):
		for char in seqs[entry][3]:
			if char < min:
				min = char
			if char > max:
				max = char
			if min < ':' or max < k:
				return (33)
			elif max > k:
				return (64)

#don't perform sum graphs when files with different encoding types are included
#this doesn't produce sum graphs, actually
def readcounts_by_quality(seqs, print_num):
	#import pdb; pdb.set_trace();
	sum = np.zeros((45,), dtype=int)
	for file in range(len(seqs)):
		encoding = get_encoding(seqs[file])
		for entry in range(1, len(seqs[file])):
			sum[average_qual(seqs[file][entry][3], encoding)] += 1
		plot_count_by_quality(sum, seqs[file][0]["filename"])

def quality_by_base(seqs, print_num):
#	import pdb; pdb.set_trace();
	for file in range(len(seqs)):
		encoding = get_encoding(seqs[file])
		sum = np.zeros((100, len(seqs[file])), dtype=int)
		for entry in range(1, len(seqs[file]) - 1):
			for i, base in enumerate(seqs[file][entry][3]):
				sum[i][entry] = average_qual(base, encoding)
		#plot_quality_by_base(sum, seqs[file][0]["filename"]);

######################################
#  	Run Quality Graphs
######################################
def run_graphs(print_num, seqs):
	total_ns = np.zeros((1500,), dtype=float)
	for file in seqs:
		total_ns += summarize_ns(file, print_num)
	plot_total_ns(total_ns, "")
	percent_gc(seqs, print_num)
	number_of_x_length(seqs, print_num)
	readcounts_by_quality(seqs, print_num)
	quality_by_base(seqs, print_num)
	



