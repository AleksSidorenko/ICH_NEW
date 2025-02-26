#!/bin/bash
#
USER=Alex
date
echo hello $USER!
pwd
ps -ef | grep biset | grep -v grep | wc -l
ls -la /etc/passwd | awk '{print $1}'

