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

valor = int (input("Entre com o ano :"))
result = valor /100
if (result > int(valor /100) ):
    result = result + 1
    print ("Século = %.0f" %result)
else:    
    print ("Século = %.0f" %result)