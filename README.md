# Programming Assignment #3

## Description
Water Bill Computation

## Instructions
1. Write a program to compute a customer’s water bill. You will ask for information on two(2) customers. Ask for
the following information:

	- customer’s name
	- type of customer (residential or commercial) – entry by user will be all lowercase letters
	- number of gallons of water used

	Residential customers are charged $1.15 per 1000 gallons of water used.
	Commercial customers are charged $0.45 per 1000 gallons of water used, but must pay an additional $100 flat fee.
	
	When printing output, convert customer type to all uppercase using the upper() string method.
	Names will be no longer than 12 characters. Gallons used will be no larger than 99999.
	Charge will be no larger than 9999.99

## Sample Run
	Enter name of customer #1: Elizabeth
	Enter gallons for customer #1: 10000
	Is customer #1 residential or commercial? residential
	------------------------------------------------------
	Enter name of customer #2: George
	Enter gallons for customer #2: 20000
	Is customer #2 residential or commercial? commercial
	------------------------------------------------------
	Name Type Gallons Charge
	------------------------------------------------------
	Elizabeth RESIDENTIAL 10000 11.50
	George COMMERCIAL 20000 109.00