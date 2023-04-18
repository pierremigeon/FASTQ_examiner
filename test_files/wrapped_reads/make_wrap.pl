#!/usr/bin/perl -w
use strict;
use Scalar::Util qw(looks_like_number);

# Author: Pierre Migeon 4/17/23
# Description: Cuts unwrapped fastq files into specified length wrapped fastq
# Usage: make_wrap.pl file_1 [file_2] wrap_int
# Comment: Use with one file or a pair of wrapped files. Original file name stored in first line of output file

if ($#ARGV < 1 || $#ARGV > 2 || !looks_like_number($ARGV[$#ARGV])) { 
	print "usage: make_wrap.pl file_1 [file_2] wrap_int\n";
	exit;
}

for my $i (0..$#ARGV - 1) {
	wrap_reads($ARGV[$i], $ARGV[$#ARGV]);
}

sub wrap_reads {
	my $fh = shift;
	my $len = shift;
	my $ofh = parse_name($fh, $len);
	open(FH, '<', $fh);
	open(OFH, '>', $ofh);
	print OFH "#ORIGINAL FILE: ${fh}\n";
	while(<FH>) {
		if ($_ !~ m/^[@+]HWI-ST/) {
			my @a = ($_ =~ /.{1,$len}/g);
			foreach (@a) {
				print OFH "$_\n";
			}
		} else {
			print OFH;
		}
	}
	close(FH);
	close(OFH);
}

sub parse_name {
	my $file_name = shift;
	my $length = shift;

	my $direction = get_direction($file_name);
	my $out_name = "wrap${length}${direction}";
	return $out_name;
}

sub get_direction {
	my $filename = shift;
	if ($filename =~ m/_F/ || $filename =~ m/\.1\./) { 
		return "_F.fq";
	} elsif ($filename =~ m/_R/ || $filename =~ m/\.2\./)  {
		return "_R.fq";
	} else {
		return ".fq";
	}
}
