#!/usr/bin/env bash
read -p "Please specify your character " char
if [[ $char =~ [[:lower:]] ]]; then
  echo "$char is in lowercase"
elif [[ $char =~ [[:upper:]] ]]; then
  echo "$char is in uppercase"
elif [[ $char =~ [0-9] ]]; then
  echo "$char is a digit"
else
  echo "$char is special character or it's more than 1 symbol entered."
fi
