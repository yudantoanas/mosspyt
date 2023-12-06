#!/bin/sh

orgName=$(cat organization.txt)
prefix=$(cat repoPrefix.txt)

for username in $(cat usernames.txt)
do
  dir=sources/$username

  echo "clonning $username"
  rm -rf $dir
  git clone git@github.com:$orgName/$prefix-$username.git $dir
done
