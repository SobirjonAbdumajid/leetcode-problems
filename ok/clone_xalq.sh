#!/bin/bash
urls=(
  "https://xalqsugurta.uz/uz/"
  "https://xalqsugurta.uz/ru/"
  "https://xalqsugurta.uz/en/"
)

for u in "${urls[@]}"; do
  wget --mirror \
       --convert-links \
       --adjust-extension \
       --page-requisites \
       --no-parent \
       --execute robots=off \
       --no-check-certificate \
       --recursive \
       --level=10 \
       --domains xalqsugurta.uz \
       "$u"
done
