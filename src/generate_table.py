#!/usr/bin/env python3
##############################################################@
#@
#      FASTQ_examiner Generate Statistics Table 
#@
##############################################################@
import os
from prettytable import PrettyTable

def generate_summary_table(seqs):
	print("");
	t = PrettyTable(left_padding_width = 2, right_padding_width = 2)
	t.add_column("File name", ["Total Reads", "Error Free", "Paired Reads", "Singletons", "Error Reads", "Paired", "Interleafed", "Wrapped"])
	for seq in seqs:
		num_paired = str(len(seq) - 1) if seq[0]["paired"] else str(0)
		t.add_column(os.path.splitext(os.path.basename(seq[0]["filename"]))[0], 
			[str(len(seq) - 1 + seq[0]["error_reads"] + seq[0]["singletons"]), 
			str(len(seq) - 1 + seq[0]["singletons"]),
			num_paired,
			str(seq[0]["singletons"]), str(seq[0]["error_reads"]), 
			str(seq[0]["paired"]), str(seq[0]["leafed"]), bool(seq[0]["wrapped"])])
	t.align = 'l'
	print(t)
