#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner manage files module
#@
#############################################@
from itertools import chain
import os

def get_file_out_name(original_file_name, extension):
	out_name = os.path.splitext(os.path.basename(original_file_name))[0]
	out_name = './out/' + out_name + extension
	return out_name

def output_processed_reads(seqs, leaf_flag):
	print(leaf_flag)

def remove_singletons(seqs):
	names, sets, out = [], [], []
	for i in range(0, len(seqs), 2):
		if seqs[i][0]["paired"] == False:
			break
		for j in range(i, i + 2):
			names.append(get_file_out_name(seqs[j][0]["filename"], '_singleton.fq'))
			sets.append(map(lambda head: head.strip("/[12]"), seqs[j][0]["headers"].keys()))
		diff = set(sets[i]).symmetric_difference(sets[i + 1])
		for j in range(i, i + 2):
			out.append([read for read in seqs[j][1:len(seqs[j])] if read[0].strip("/[12]") in diff])
			with open(names[j], 'w') as f:
				f.write("\n".join(list(chain.from_iterable(out[j]))))
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
