#!/usr/bin/env bash
read -p "Please specify your number " num
if [[ num -gt 15 && num -lt 45 ]]; then
  echo "Your number in good range."
else
  echo "Your number is out of range."
fi
