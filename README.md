#### Status update 7/20/23:
I've been working on C/C++ projects for a few weeks and I'm jumping back into this (at least briefly to polish it). I noticed that some of the tests were broken, so I've updated several of them now so that the curious may run the program to get an idea for how it works.

Running demo/tests:
```
bash run_test.sh [0-8]
```
simply run the above bash script with a number between 0-8. Tests above 8 demonstrate the program fails using wrapped input files, so this is the next priority fix.

# FASTQ_examiner
### A tool to filter and produce summary statistics and charts for FASTQ files

*tool in developement...*

FASTQ examiner is a tool written in python to do basic sanity checking of FASTQ files. Files are checked for validity, wrapping, and truncation. Wrapped files are unwrapped, and any malformed or truncated entries in the FASTQ files are removed. Subsequently, sequence read summary statistics and graphs are produced.

```
# usage: fastq_examiner.py [-h] [-v] [-e EMAIL] -f1 FASTQ_1 [-f2 FASTQ_2] [-c] [-q] [-i]
# Example command for demonstration purposes:
./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -i
```

Diagnostic graphs produced can be useful for understanding fastq data quality or other status. For example, extreme 5' nucleotide bias in this case suggests sequencing adapters have yet to be removed:
![graph](https://user-images.githubusercontent.com/8321639/70365885-95504880-1848-11ea-9321-5fb1756d2e7f.png)

**I used the following tool to quickly make some random fastq files to play with during development:** <br />
M. Frampton, R. Houlston (2012) Generation of Artificial FASTQ Files to Evaluate the Performance of Next-Generation Sequencing Pipelines.
*PLoS ONE* 7 (11), http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0049110

**See the following for a description of the fastq format:**<br />
Cock PJ, Fields CJ, Goto N, Heuer ML, Rice PM. The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants. Nucleic Acids Res. 2010;38(6):1767–1771. doi:10.1093/nar/gkp1137
