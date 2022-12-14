import os
os.system('cls')

# player score
score = 0

# questions, answers and explanations
questions = [
    ("\n\n\n1- What is an object in programming?\nA) An object is a collection of data and associated behavior\nB) An object is a type of function that contains data and is used as a blueprint \nto create classes\n", "A","\nAn object is not a type of function. In object-oriented programming, an object is a collection of data and associated behavior (or methods) that operate on that data. \nObjects are used to represent real-world things and concepts, and provide a way to organize and structure code."),
    ("\n\n\n2- Select the group that has only Python data types.\nA) Integer, map, filter, zip, reduce\nB) dictionary, generator, coroutine, asyncio\nC) Integer, float, string, list, tuple, dictionary\nD) list, dictionary, string, attribute, method\n", "C", "\nInteger, float, string, list, tuple, dictionary are all data types"),
    ('\n\n\n3- Which example uses list comprehension to print a list?\n\nA)\n\nfruits = ["apple", "banana", "cherry", "kiwi", "mango"]\nnewlist = []\nfor x in fruits:\n  if "a" in x:\n    newlist.append(x)\nprint(newlist)\n\nB)\n\nfruits = ["apple", "banana", "cherry", "kiwi", "mango"]\nnewlist = [x for x in fruits if "a" in x]\nprint(newlist)\n',"B","\nList comprehension syntax is [item for item in array] and can include if/else etc. \nstatements to achieve the same result as a for loop (iteration)"),
    ('\n\n\n4- T or F\nExceptions are errors or anomalies that occur during the execution of a program.\n',"T","\nExceptions are errors or anomalies that occur during the execution of a program.\nThese exceptions can be handled using try-except blocks,\nwhich allow you to specify what code to run when an exception occurs."),
    ('\n\n\n5- What would be the outcome of this code?\n10 % 2\n\nA)5\nB)2\nC)20\nD)0\n','D','\nThe result of the expression 10 % 2 is 0. This is because 10 divided by 2 is 5 with a remainder of 0.\nThe mod operator returns the remainder of the division operation, which in this case is 0.\n'),
    ('\n\n\n6- Which one of the provided answers will print "Monkey"\n\nmonkey_business = [1,["Money",32,97],3,[100,20,3,"$%^("],5,[9,["test",["Monkey"]]]]\n\nA) print(monkey_business[5][1][1])\nB) print(monkey_business[12])\nC) print(monkey_business[6][2][2])\nD) print(monkey_business[9][1])\n',"A",'\nprint(monkey_business[5][1][1]) would access the nested lists that Monkey is in'),
    ("\n\n\n7- What does this code do and return?\n\nimport re\ntxt = 'n3eD to Se4rcH t3XT'\nq = re.findall(r'[0-9]',txt)\nprint(q)\n\nA) imports recursion operations module and prints numbers 0-9 if they are in the text\nB) imports regular expression operations module and prints list of numbers in text\nC) imports recursion operations module and returns 'neD to SercH tXT'\nD) None of above\n",'B',"\nThis imports regular expression operations module and prints list of numbers in text"),
    ('\n\n\n8- Choose the correct naming convention for a variable.\n\nA) My_Variable\nB) my_Variable\nC) MyVariable\nD) my_variable','D',"\nThe correct naming convention for a variable in Python is D) my_variable. \nIn Python, variables, functions, and methods should be written in lowercase, \nwith words separated by underscores."),
    ('\n\n\n9- T or F\nprint("5 * 50") --> 250','F',"\nFalse. The statement print('5 * 50') will not print the result of the multiplication \noperation 5 * 50, but will instead print the string '5 * 50' to the console."),
    ('\n\n\n10- What does this function do\n\ndef question(arr):\n    odds = sorted(list(filter(lambda n: n%2!=0,arr)),reverse=True)\n    return [n if n%2==0 else odds.pop() for n in arr]\n\nprint(question([1,3,3,4,7,6,5,1,2,9]))print(question([1,3,3,4,7,6,5,1,2,9]))\n# --> [1, 1, 3, 4, 3, 6, 5, 7, 2, 9]\n\nA) Sorts the array from smallest int to largest using list comprehension, \nthe .pop() and the reverse=True method. \n\nB) Creates a reversed sorted list of the odd numbers from the original array, \nif the number in the original array is not even, it replaces the original odd with the sorted odd.\n\nC) Prints a sorted list of numbers that uses (lambda n: n%2!=0,arr) to remove the even numbers from the list\n','B',"\n\n\nThe correct answer is B) Creates a reversed sorted list of the odd numbers from the original array,\n if the number in the original array is not even, it replaces the original odd with the sorted odd.\n\nThe question() function takes a list of numbers as an argument and performs the following operations:\n\nIt uses the filter() method and a lambda function to remove all even numbers from the list,\nand then uses the sorted() function to sort the remaining odd numbers in descending order (i.e. from largest to smallest).\nIt uses a list comprehension to iterate over the original list, and replaces each odd number \nwith the next number from the sorted list of odds (using the pop() method to remove the number \nfrom the list after it has been used). If the current number is even, it is left unchanged.\nIt returns the resulting list of numbers.\nTherefore, when the question() function is called with the list [1,3,3,4,7,6,5,1,2,9], it will create a \nreversed sorted list of the odd numbers from the original array (i.e. [7,5,3,3,1,1]), \nand will then replace each odd number in the original\n")
]

def ask_question(ques, ans, ex):
    '''Takes in a question, its answer and explanation, if the user selects the correct answer, their score will go up by 1, else print explanation'''
    print('_____________________________________________________________________________')
    print(ques)
    answer = input("Answer: ")
    if answer.lower() == ans.lower():
        # add 1 to correct
        print(f"\nCorrect!{ex}")
        global score
        score += 1
    else:
        print(f'\nIncorrect!{ex}')

# loop through ever question and use the ask_question function
for ques, ans, ex in questions:
    ask_question(ques, ans, ex)

# display score
print(f'You got {score} answers right out of 10')