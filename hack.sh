#!/bin/bash

while read -r line; do
	ip="$line"
	python hackprinter.py $ip -A
done < 'attack_ip.txt'