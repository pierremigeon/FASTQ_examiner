#!/usr/bin/env python3
#############################################@
#@
#	FASTQ_examiner manage files module
#@
#############################################@
from itertools import chain

def remove_singletons(seqs):
	for i in range(0, len(seqs), 2):
		if seqs[i][0]["paired"] == False:
			break
		diff = set(seqs[i][0]["headers"].keys()).symmetric_difference(seqs[i + 1][0]["headers"].keys())
		out = [read for read in seqs[i][1:len(seqs[i])] if read[0] in diff]
		with open('./singletons', 'w') as f:
			f.write("\n".join(list(chain.from_iterable(out))))
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
