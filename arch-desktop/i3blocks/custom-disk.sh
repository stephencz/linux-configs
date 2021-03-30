#!/bin/bash

REMAINING=$(df -h | grep '/dev/sda2' | awk -F' ' '{print $4}')

echo "${REMAINING}B"
echo "${REMAINING}B"

exit 0
