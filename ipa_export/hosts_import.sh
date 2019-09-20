#!/bin/bash

FN=$1
OTP=MyOnetimePassword

RE_HOSTNAME="Host name:\s+(.*)$"

name=""

while read line; do
    if [[ $line =~ "$name" ]]; then
        if [[ -n "$name" ]]; then
            echo "Adding $name"
            ipa host-add $name --password $OTP --force
        fi
        name=${BASH_REMATCH[1]}
    fi
done < $FN
echo "Adding $name"
ipa host-add $name --password $OTP --force

