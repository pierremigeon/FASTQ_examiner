#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner manage files module
#@
#############################################@
from itertools import chain
import os

def output_processed_reads(seqs, leaf_flag):
	#print(leaf_flag)

def remove_singletons(seqs):
	for i in range(0, len(seqs), 2):
		if seqs[i][0]["paired"] == False:
			break
		file_1_name = os.path.splitext(os.path.basename(seqs[i][0]["filename"]))[0]
		file_1_name = './out/' + file_1_name + '_singleton.fq'
		file_2_name = os.path.splitext(os.path.basename(seqs[i + 1][0]["filename"]))[0]
		file_2_name = './out/' + file_2_name + '_singleton.fq'
		set1 = map(lambda head: head.strip("/[12]"), seqs[i][0]["headers"].keys())
		set2 = map(lambda head: head.strip("/[12]"), seqs[i + 1][0]["headers"].keys())
		diff = set(set1).symmetric_difference(set2)
		out1 = [read for read in seqs[i][1:len(seqs[i])] if read[0].strip("/[12]") in diff]
		out2 = [read for read in seqs[i + 1][1:len(seqs[i + 1])] if read[0].strip("/[12]") in diff]
		with open(file_1_name, 'w') as f:
			f.write("\n".join(list(chain.from_iterable(out1))))
		f.close()
		with open(file_2_name, 'w') as f:
			f.write("\n".join(list(chain.from_iterable(out2))))
		f.close()
		

def order_files(seqs):
	seqs.sort(key=lambda x: x[0]['head'])
	for i in reversed(range(0, len(seqs))):
		seqs[i][0]["paired"] = True
		if seqs[i][0]["head"] not in seqs[i - 1][0]["head"] \
			and seqs[i - 1][0]["head"] not in seqs[i][0]["head"]:
				if i == len(seqs) or seqs[i][0]["head"] not in seqs[i + 1][0]["head"] \
					and seqs[i + 1][0]["head"] not in seqs[i][0]["head"]:
						seqs[i][0]["paired"] = False
						seqs.append(seqs.pop(i))
