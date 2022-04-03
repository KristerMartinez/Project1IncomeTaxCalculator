# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:52:41 2022

@author: Krister Martinez

Project 1 - Income Calculator
"""

grossIncome=float(input("Enter the gross income: "))
dependentNum=int(input("Enter the number of dependents: "))

totalIncome=grossIncome-10000-(dependentNum*3000)

totalTax=(totalIncome*20)/100

print("The income tax is $ "+str (totalTax))

