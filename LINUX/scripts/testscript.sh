#!/bin/bash

#for i in {1..5}
#do
#	mkdir /Users/laimamur/test_dir/Dir$i
#	echo "Dir$i created"
#	for j in {1..5}
#	do
# 	   touch /Users/laimamur/test_dir/Dir$i/File$j.txt 
#	   date +'%H-%M-%S' >> /Users/laimamur/test_dir/Dir$i/File$j.txt
#	   # sleep 1		
#	   echo "File$j created"
#	done 
#done

# ls /Users/laimamur/test_dir/*

tar czvf /tmp/arc-140225.tar.gz /Users/laimamur/test_dir

tar tvf /tmp/arc-140225.tar.gz

mkdir -p /tmp/arc
tar xvf /tmp/arc-140225.tar.gz -C /tmp/arc		      
