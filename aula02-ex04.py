import os
os.system('cls')
"""
Exercicio 4
– Given a year, return the century it is in.
 The first century spans from the year 1 up to and including the year 100, the second 
 - from the year 101 up to and including the year 200, etc.
– Example 
• For year = 1905, the output should be centuryFromYear(year) = 20; 
• For year = 1700, the output should be centuryFromYear(year) = 17
"""

def centuryFromYear(year):
    century = year /100
    if (century > int(year /100) ):
        century = century + 1
        print ("Século = %.0f" %century)
    else:    
        print ("Século = %.0f" %century)

centuryFromYear(int(input("Entre com o ano :")))
