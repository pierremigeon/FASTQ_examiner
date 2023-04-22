#!/usr/bin/bash
###################################################################################################
# Description: Check for all python dependencies and install. Requires pip3			  #
# Usage: to run script, execute '.  check_dependencies.sh' or 'source check_dependencies.sh'	  #
# Author: Pierre Migeon April 2023								  #
###################################################################################################

if [[ ! $(which pip3) ]]; then
	echo "pip3 is not installed. Install to continue.";
	read -n 1 -p "Install? (y/n)" install_check;
	echo;
	if [ $install_check == 'y' ]; then
		python3 -m ensurepip;
	else
		exit 0;
	fi
fi

if [ $(pip3 show pipreqs | wc -l | sed 's/ //g') == 0 ];
then
	pip3 install pipreqs
fi

#Alias pipreqs command
alias pipreqs='python3 -m pipreqs.pipreqs'

#run pipreqs to generate requirements file
pipreqs ..
pipreqs .
cat ../requirements.txt >> ./requirements.txt
cat ./requirements.txt | sort | uniq > tmp.txt
mv tmp.txt ./requirements.txt
rm ../requirements.txt

#Install requirements
pip3 install -r requirements.txt

#remove requirements file:
rm requirements.txt
