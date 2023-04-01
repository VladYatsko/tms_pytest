#!/usr/bin/env bash
echo "Do you want to install python?"
select choice in "Yes" "No"; do
  case $choice in
  Yes) echo "You've decided to install python"; break;;
  No) echo "Get out and close the door"; break;;
  *) echo "Strange selection" ;;
  esac
done
