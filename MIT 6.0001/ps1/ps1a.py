# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:09:36 2022

@author: setonliu
"""

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

total_cost = total_cost*0.25
current_savings = 0
r = 0.04

money_saved = monthly_salary*portion_saved


months = 0
while current_savings < total_cost:
    months +=1
    current_savings += current_savings*r/12 
    current_savings += money_saved


print("Number of months", months)