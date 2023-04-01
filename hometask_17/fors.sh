#!/usr/bin/env bash
for i in {11..1}; do
  if [ $(($i % 2)) -eq 0 ]; then
    echo "$i"
  fi
done
