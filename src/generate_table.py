#!/usr/bin/env python3
##############################################################@
#@
#      FASTQ_examiner Generate Statistics Summary Tables      
#@
##############################################################@

def table(seq):
	print("\n" + seq[0]["filename"] + " Summary Statistics")
	print("| Number Reads + Paired + Interleafed + Wrapped Reads |")
	print("|-----------------------------------------------------|")
	print("|\t", str(len(seq) - 1), "\t", str(seq[0]["paired"]), "\t   ", str(seq[0]["leafed"]), "\t\t" + str(seq[0]["wrapped"]), "    |")
	print("\n")

def generate_summary_table(seqs):
	for seq in seqs:
		table(seq)
