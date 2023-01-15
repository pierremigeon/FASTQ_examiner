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
import pdb
#############################################
#program modules
import src.format_check as fc
import src.put_in_struct as pis
import src.run_QC_checks as rqcc
import src.run_graphs as rg

######################################
#  Help/Usage formatting and get args
######################################
def get_args():
	parser = argparse.ArgumentParser(
		add_help = False,
		formatter_class = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position = 80),
		description="""Description: Check the validity of FASTQ files, correct formating errors, and produce summary statistics.""", 
		epilog="""Created by Pierre Migeon, updated winter 2023
		\n"""
		)
	help_arguments = parser.add_argument_group('help arguments')
	help_arguments.add_argument('-h', '--help', action='help', help='\tshow this help message and exit.')
	help_arguments.add_argument('-v', '--version', action='version', help='\tshow the current program version.')
	help_arguments.add_argument('-e', '--email', help='\tsend an email to the program author')
	parser.add_argument('-f1', '--forward', dest='fastq_1', help="""\tThe path to the first fastq""", required=True)
	parser.add_argument('-f2', '--reverse', dest='fastq_2', help="""\tThe path to the second fastq""", required=False)
	parser.add_argument('-c', help="""\tcorrect invalid files""")
	parser.add_argument('-q', help="""\tcheck validity of files and then exit""")
	parser.add_argument('-i', '--plot_individual', dest='plot_num', help="""\tproduce individual summary plots""", required=False, action='store_true')
	if '-h' or '--help' in sys.argv:
		print("")
	args = parser.parse_args()
	return args

######################################
#  Main
######################################
def main():
	args = get_args()
	files = []
	forward_file = args.fastq_1
	files.append(forward_file)
	if args.fastq_2:
		reverse_file = args.fastq_2 
		files.append(reverse_file)
	fc.fastq_format_check(files)
	seqs = []
	for file in files:
		seqs.append(pis.put_in_struct(file))
	rqcc.run_QC_checks(files, seqs)
	#Summary_table(seqs) (coming soon)
	rg.run_graphs(files, args.plot_num, seqs)

######################################
#  Call Main
######################################
if __name__ == '__main__':
	main()
