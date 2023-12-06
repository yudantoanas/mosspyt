#!/bin/sh

# STILL INCOMPLETE. DO NOT RUN THIS!
exit

# clone repo
bash ./clone.sh

# check files
if [[ ! -f usernames.txt || ! -f filePrefix.txt || ! -f repoPrefix.txt || ! -f organization.txt ]]
    then
        echo 'Make sure these file exists'
        echo ' - usernames.txt'
        echo ' - filePrefix.txt'
        echo ' - repoPrefix.txt'
        echo ' - organization.txt'

        exit
fi

# prompt
read -p "py or ipynb? (default: ipynb)
(p)py/(n)ipynb/(c)Cancel:- " choice

# execute extractor
case $choice in
[pP]* ) python scriptExtractor.py ;;
[nN]* ) python notebookExtractor.py ;;
[cC]* ) echo "operation cancelled" ;;
*) exit ;;
esac

# run MOSS script
./moss.pl -l python -c "MOSS Results" ./outputs/*.py 