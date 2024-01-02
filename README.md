## Project Title: PyFinElectionMagic 🚀

## Overview
PyFinElectionMagic is a Python script designed for financial data analysis (PyBank) and election results (PyPoll). It provides insights into financial trends and election outcomes based on the input data.

# Features

# PyBank
* Calculates total months in the dataset
* Determines the net total profit/loss over the entire period.
* Computes the average change in profit/loss.
* Identifieds the greatest increase and decrease in profits.

## PyPoll
* Counts the total number of votes cast.
* Determines the percentage of votes and total votes for each candidate.
* Declares the election winner.

## Usage
1. Ensure you have Python installed on your machine.
2. Clone the repository.
```bash
git clone https://github.com/your-username/PyFinElectionMagic.git
```
3. Navigate the project directory.
```bash
cd PyFinElectionMagic
```
4. Run the PyBank script.
```bash
python PyBank.py
```
5. Run the PyPoll script.
```bash
python PyPoll.py
```

## Data
*Financial data: The PyBank script analyzes a CSV file containing financial data with columns for months and profit/loss values.
*Election data: The PyPoll script analyzes a CSV file containing election data with columns for voter ID, county, and candidate.

## Output
* PyBank: Outputs financial analysis results to the console and a text file in the 'PyBank/analysis' directory.
* PyPoll: Outputs election results to the console and a text file in the 'PyPoll/analysis' directory.

## Dependencies
* Python 3.x
* CSV module

## Future Enhancements
* Graphical visualization of financial trends.
* Dynamic candidate input handling for PyPoll.

## Contributors
* Erika Walker

## Acknowledgements
* This project was inspired by the need for quick and insightful analysis of financial and election data using Python.
