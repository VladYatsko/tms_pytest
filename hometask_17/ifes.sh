#!/usr/bin/env bash
if (($#<1)); then
  echo "This script requires 1 argument with path to file or directory!";
  exit
fi
if [[ -d $1 || -a $1 ]]; then
  echo "File or directory exists"
else
  echo "File or directory is not exist"
fi