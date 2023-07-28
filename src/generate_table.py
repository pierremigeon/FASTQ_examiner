#!/usr/bin/env python3
##############################################################@
#@
#      FASTQ_examiner Generate Statistics Summary Tables      
#@
##############################################################@
#there has got to be a better way to do this...
import os
from prettytable import PrettyTable

def generate_summary_table(seqs):
	t = PrettyTable(["File name", "Number Reads", "Paired", "Interleafed", "Wrapped", "Error Reads"])
	for seq in seqs:
		t.add_row([ os.path.basename(seq[0]["filename"]) , str(len(seq) - 1), str(seq[0]["paired"]), str(seq[0]["leafed"]), str(seq[0]["wrapped"]), str(seq[0]["error_reads"])])
	print(t)
