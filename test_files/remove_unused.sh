#!/bin/bash
#author: Pierre Migeon 4/17/23
#description: Remove test files from this directory that aren't called in the test script
#usage: bash ./remove_unused.sh 

for file in ./*; do if [ $(grep $file ../run_test.sh | wc -l | sed 's/ +//g') == 0 ]; then if [ ! -d $file ]; then rm $file; fi ; fi; done
