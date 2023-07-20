#!/usr/bin/env python3
##############################################################@
#@
#      FASTQ_examiner Generate Statistics Summary Tables      
#@
##############################################################@
#there has got to be a better way to do this...

def table(seq):
	print("\n" + seq[0]["filename"] + " Summary Statistics")
	print("");
	print("|-------------------------------------------------------------------|")
	print("| Number Reads + Paired + Interleafed + Wrapped Reads + Error Reads |")
	print("|--------------|--------|-------------|---------------|-------------|")
	print("|     ", str(len(seq) - 1), "\t ", str(seq[0]["paired"]), "     ", str(seq[0]["leafed"]), "\t      " + str(seq[0]["wrapped"]), "\t     " + str(seq[0]["error_reads"]), "     |")
	print("|-------------------------------------------------------------------|")
	print("\n")

def generate_summary_table(seqs):
	for seq in seqs:
		table(seq)
