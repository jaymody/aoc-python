#!/bin/bash

years=(2015 2016 2017 2018 2019 2020 2021 2022 2023 2024)
read -rp "Enter your Advent of Code session cookie: " session_cookie

for year in "${years[@]}"; do
    for day in {1..25}; do
        input_url="https://adventofcode.com/$year/day/$day/input"
        output_path=$(printf "%s_%02d.txt" "$year" "$day")
        echo "Downloading: $input_url to $output_path"
        curl --silent --cookie "session=$session_cookie" "$input_url" -o "$output_path"
    done
done

echo "Download complete!"
