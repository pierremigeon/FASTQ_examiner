#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner manage files module
#@
#############################################@
from itertools import chain
import os

# Tests to write: 
# 	1) Does the sorting of the paired lists work?

def get_file_out_name(original_file_name, extension):
	out_name = os.path.splitext(os.path.basename(original_file_name))[0]
	if not os.path.isdir('./out/' + out_name):
		os.mkdir('./out/' + out_name)
	out_name = './out/' + out_name + '/' + out_name + extension
	return out_name

def get_common_name(name_1, name_2):
	common = os.path.commonprefix([name_1, name_2])
	if common[-1] == '_':
		common = common.rstrip('_')
	return common

def interleaf(seqs):
	for i in range(0, len(seqs), 2):
		if seqs[i][0]["paired"] == False:	
			break
		out = list(chain.from_iterable(list(map(list, zip(seqs[i], seqs[i + 1])))))
		common_name = get_common_name(out[0]["filename"], out[1]["filename"])
		out_name = get_file_out_name(common_name, '_leaf_final.fq')
		with open(out_name, 'w') as f:
			f.write('\n'.join(chain.from_iterable(out[2:len(out)])) + '\n')
	return i

def output_processed_reads(seqs, leaf_flag):
	i = 0
	if leaf_flag:
		i = interleaf(seqs)
	new_line = '\n'
	for j in range(i, len(seqs)):
		out_name = get_file_out_name(seqs[j][0]["filename"], '_final.fq')
		with open(out_name, 'w') as f:
			f.write('\n'.join(chain.from_iterable(seqs[j][1:len(seqs[j])])) + '\n')
		f.close()

def split_leafed(seqs):
	new_seqs = []
	for i in range(0, len(seqs)):
		if seqs[i][0]["leafed"]:
			seqs[i][0]["middle"] += 1
			new_seqs.append(seqs[i][0:seqs[i][0]["middle"]])
			new_seqs.append([seqs[i][0]] + seqs[i][seqs[i][0]["middle"]:])
		else:
			new_seqs = seqs 
		return new_seqs

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
			seqs[j] = [read for read in seqs[j] if list(read)[0].strip("/[12]") not in diff]
			if out[-1]:
				with open(names[j], 'w') as f:
					f.write("\n".join(list(chain.from_iterable(out[j]))) + '\n')
				f.close()
			seqs[j][0]["singletons"] = len(out[j])

def order_files(seqs):
	seqs.sort(key=lambda x: x[0]['head'])
	for i in reversed(range(0, len(seqs))):
		seqs[i][0]["paired"] = True
		if i == 0 or seqs[i][0]["head"] not in seqs[i - 1][0]["head"] \
			and seqs[i - 1][0]["head"] not in seqs[i][0]["head"]:
				if i + 1 == len(seqs) or seqs[i][0]["head"] not in seqs[i + 1][0]["head"] \
					and seqs[i + 1][0]["head"] not in seqs[i][0]["head"]:
						seqs[i][0]["paired"] = False
						seqs.append(seqs.pop(i))
