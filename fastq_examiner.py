#!/usr/bin/env python3 
#############################################@
#@
#	FASTQ_EXAMINER
#
#	A program to assess FASTQ format
#	correctness and assess fastq quality.
#
#	Also written as an exercise in order to learn Python.
#	Created by Pierre Migeon
#
#	Usage: fastq_examiner.py [-h] [-v] [-e EMAIL] -f1 FASTQ_1 [-f2 FASTQ_2] [-c C] [-q Q] [-i]
#	./fastq_examiner.py --help for more detailed usage
#@
#############################################@
import sys
import argparse
#############################################
from src import put_in_struct as pis
from src import run_QC_checks as rqcc
from src import run_graphs as rg
from src import manage_files as mf
from src.generate_table import generate_summary_table

######################################
#  Help/Usage formatting and get args
######################################
def get_args():
	parser = argparse.ArgumentParser(
		add_help = False,
		formatter_class = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position = 80),
		description="""Description: Check the validity of FASTQ files, correct formating errors, and produce summary statistics.""", 
		epilog="""Created by Pierre Migeon, most recent update summer 2023
		\n"""
		)
	help_arguments = parser.add_argument_group('help arguments')
	help_arguments.add_argument('-h', '--help', action='help', help='\tshow this help message and exit.')
	help_arguments.add_argument('-v', '--version', action='version', help='\tshow the current program version.')
	help_arguments.add_argument('-e', '--email', help='\tsend an email to the program author')
	parser.add_argument('fastq_1', nargs='*')
	parser.add_argument('-f1', '--forward', dest='fastq_2', help="""\tThe path to the first fastq""", required=False)
	parser.add_argument('-f2', '--reverse', dest='fastq_3', help="""\tThe path to the second fastq""", required=False)
	parser.add_argument('-c', help="""\tcorrect invalid files""")
	parser.add_argument('-q', help="""\tcheck validity of files and then exit""")
	parser.add_argument('-f', '--full', dest='plot_num', help="""\toutput all plots""", required=False, action='store_true')
	parser.add_argument('-nv', help="""\tSuppress graphical output""", required=False, action='store_true')
	parser.add_argument('-leaf', help="""\tPaired reads are output in interleaved format""", required=False, action='store_true')
	if '-h' or '--help' in sys.argv:
		print("")
	args = parser.parse_args()
	return args

def is_empty(seqs):
	for entry in seqs:
		if len(entry) > 1:
			return False
	return True

def trim_empty(seqs):
	seqs = [element for element in seqs if len(element) > 1]
	return seqs

#Check to see if the seqs file is empty when you output the error reads, so that you can specify to the user exactly if all reads have errors -vs- no reads at all in the files.
######################################
#  Main
######################################
def main():
	args = get_args()
	seqs = []
	for file in [ *args.fastq_1, args.fastq_2, args.fastq_3 ]:
		if file:
			seqs.append(pis.put_in_struct(file))
	if is_empty(seqs):
		sys.exit("Either all input files are empty, or all reads have errors! exiting...")
	seqs = trim_empty(seqs)
	seqs = mf.split_leafed(seqs)
	mf.pair_and_order_files(seqs)
	mf.remove_singletons(seqs)
	mf.output_processed_reads(seqs, args.leaf)
	generate_summary_table(seqs)
	if not args.nv:
		rg.run_graphs(args.plot_num, seqs)

######################################
#  Call Main
######################################
if __name__ == '__main__':
	main()
