# FASTQ_examiner
### A tool to filter and produce summary statistics and charts for FASTQ files

FASTQ examiner is a tool written in python to do basic sanity checking of FASTQ files. Files are checked for validity, wrapping, and truncation. Wrapped files are unwrapped, and any malformed or truncated entries in the FASTQ files are removed. Subsequently, sequence read summary statistics and graphs are produced.

```
# usage: fastq_examiner.py [-h] [-v] [-f1] FASTQ_1 [-f2 FASTQ_2] [-c] [-q] [-f] [-nv]

# Example command for demonstration purposes:
./fastq_examiner.py -f1 ./test_files/C1.1.fastq -f2 ./test_files/C1.2.fastq -i
```
The tool generates numerous sumary statistics and graphs for input fastq files. It can also help determine different relationships between files, such as paired status, and sorts and pairs files automatically regardless of input order.

Summary table:

<img width="585" alt="Screen Shot 2023-11-27 at 8 17 12 AM" src="https://github.com/pierremigeon/FASTQ_examiner/assets/107828529/ca1965f1-dd8d-4854-94fe-575d23660723">


Distribution of Quality scores over each base (all reads):
<img width="1132" alt="Screen Shot 2023-11-27 at 8 11 42 AM" src="https://github.com/pierremigeon/FASTQ_examiner/assets/107828529/3134aeb3-67f0-4a25-a019-a7b5fc669162">
Diagnostic graphs produced can be useful for understanding fastq data quality or other status. For example, extreme 5' nucleotide bias in this case suggests sequencing adapters have yet to be removed:
![graph](https://user-images.githubusercontent.com/8321639/70365885-95504880-1848-11ea-9321-5fb1756d2e7f.png)

I have written a series of tests to demonstrate this functionality of this project:
```
#check missing requirements and install:
cd ./src
bash check_dependencies.sh
#Running demo/tests (from base directory):
bash run_test.sh [-2 - 29]
```
Use the run_test.sh script with a number between -2 - 29 to run demo tests.
### Dependencies:
Check and install any missing python libraries using the `./src/check_dependencies.sh` script.

### References:
**I used the following tool to quickly make some random fastq files to play with during development:** <br />
M. Frampton, R. Houlston (2012) Generation of Artificial FASTQ Files to Evaluate the Performance of Next-Generation Sequencing Pipelines.
*PLoS ONE* 7 (11), http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0049110

**See the following for a description of the fastq format:**<br />
Cock PJ, Fields CJ, Goto N, Heuer ML, Rice PM. The Sanger FASTQ file format for sequences with quality scores, and the Solexa/Illumina FASTQ variants. Nucleic Acids Res. 2010;38(6):1767–1771. doi:10.1093/nar/gkp1137
