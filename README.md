# assignment-5
task 1 :
    I made a dictionary called studs that stores student names as keys and their marks as values.
    Then I asked the user to enter a student’s name using input() and saved it in a variable called usrinp.
    Since dictionary keys are in lowercase, I converted the user input to lowercase using .lower() and saved that in lowcs.
    I used an if statement to check if the lowercase name exists in the dictionary studs.
    If the name is found, I used a formatted print statement to show that student’s marks out of 100.
    If the name isn’t in the dictionary, I printed a message saying the name is not in the list.


task 2 :
    I started by making an empty list called org_list.
    I used a try block because I wanted to catch any invalid input like letters or symbols.
    Inside the try, I asked the user to enter a number using input() and converted it to int, then saved it as n.
    I used a for loop from 1 to n (inclusive) and added each number to org_list using .append().
    After building the list, I printed it to show the original numbers.
    Then I checked if n is even or odd:
    If even, I did n // 2 to get the half.
    If odd, I used (n + 1) // 2 to include the middle number.
    I sliced the original list using [:num1] to get the first part and stored it in slcd_list.
    I printed the sliced list to show the extracted portion.
    I used .reverse() to reverse the slcd_list.
    This reversed the list in place (didn't return a new list).
    Then I printed the reversed list to show the final result.
    If the user enters anything that's not an integer, the except ValueError block runs and shows a message:
    "Please enter an integer"
