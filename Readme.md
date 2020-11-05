# SSD Assignment 3B

Github Repo Link - [https://github.com/abhijeet181995/SSD-Assignmnet-3a/tree/PartB]

Commit File Change for Detailed File Difference [https://github.com/abhijeet181995/SSD-Assignmnet-3a/pull/1/files]

## Question 1

- Name is assumed to be the employee id (001-999)
- Employee Ids are to be separted with spaces

## Line Changes Question 1

- Line 18 -Added list of parents parent_list=[].
- Line 29 -Added list of common parents of all the employees by taking intersection of all parents
- Line 39 -Added Loop for printing all the level difference of all the employees and parent empolyees

## Question 2

- The data format should be given as mentioned in the assignment
- date_calculator.txt should be present in the same directory and should be readable as well.4
- commandline is to provided for dd/mm/yyyy or mm/dd/yyyy else default format of alphanumeric will be used

## Line Changes Question 2

- Line 48 -Added a flag parameter the holds the value of tyoe of parameter dd/mm/yyyy or mm/dd/yyyy or alphanumeric
- Line 7-17 - added new conversion of the mm/dd/yyyy format in the convertdate function.

## Question 3

- Make sure Employee1.txt Employee2.txt are present in the [Employee] folder in the same directory.
- Name of the Employee file and Employee name should be same.
- Dates should be same otherwise individual slot are given but no common slot printed.
- The format provided in the assignment should be same as described in the assignment.

## Line Changes Question 3

- Line 2 - import os added
- Line 90- os.listdir() is used to get the list of all the files in the employee directory
- Line 91- list_files_path list all the file path
- Line 94-97- list_dic contains all the files information in dictionary format
- Line 100-employee_names contains the name of all employee same as file name
- Line 102- flag for checking all the dates are same or not
- Line 114- contains list of all free slots of all employees
- free1 free2 available slot of Employee1 and Employee2
- Line 112- free3 contains free slot of all the employees
- Line 119-125- loop for all employee free slot and common free3 slot
- Line 135-140- checking flag is set or not
- Line 31-Output fuction not has new parameter employee_names and list_free
- Line 33-37- Writing all the free slots of available employee in a loop
