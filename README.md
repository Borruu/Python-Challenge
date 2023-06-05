# Python

## Setup

This project contains a directory for each Python challenge: **PyBank** and  **PyPoll**.

* Each folder contains:

  * File `main.py`. This is the main script to run for each analysis.
  * A `Resources` folder that contains the CSV files used.
  * An `analysis` folder that contains a text file of results from the analysis.

## Part One: PyBank

Task: create a Python script to analyse the financial records of a company [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".

The script calculates each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

The analysis is printed to the terminal and exported as text file of results.

## Part Two: PyPoll

Task: help a small, rural U.S. town modernise its vote counting process, using a given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

The script calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

The analysis is printed to the terminal and exported as text file of results.

## Considerations

* The datasets for these challenges are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more robust options for handling big data.


## References

Dataset created by Trilogy Education Services, a 2U, Inc. brand.

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
