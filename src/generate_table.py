#!/usr/bin/env python3
##############################################################@
#@
#      FASTQ_examiner Generate Statistics Table 
#@
##############################################################@
import os
from prettytable import PrettyTable

def calc_base_pairs(seqs):
	raw_len = sum(seqs[0]["seq_lens"])
	precision = int((len(str(raw_len)) - 1) / 3) * 3
	raw_len = round(raw_len, -precision)
	raw_len = raw_len * 10 ** -precision
	scale = " Tb" if precision == 12 \
		else " Gb" if precision == 9 \
		else " Mb" if precision == 6 \
		else " Kb" if precision == 3 \
		else " bp"
	return str(int(raw_len)) + scale

def generate_summary_table(seqs):
	print("");
	t = PrettyTable(left_padding_width = 2, right_padding_width = 2)
	t.add_column("File name", ["Total Bases", "Total Reads", "Error Free", "Paired Reads", "Singletons", "Error Reads", "Paired", "Interleafed", "Wrapped"])
	for seq in seqs:
		num_paired = str(len(seq) - 1) if seq[0]["paired"] else str(0)
		base_pairs = calc_base_pairs(seq)
		t.add_column(os.path.splitext(os.path.basename(seq[0]["filename"]))[0], 
			[base_pairs,
			str(len(seq) - 1 + seq[0]["error_reads"] + seq[0]["singletons"]), 
			str(len(seq) - 1 + seq[0]["singletons"]),
			num_paired,
			str(seq[0]["singletons"]), str(seq[0]["error_reads"]), 
			str(seq[0]["paired"]), str(seq[0]["leafed"]), bool(seq[0]["wrapped"])])
	t.align = 'l'
	print(t)
