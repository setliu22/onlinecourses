# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:09:36 2022

@author: setonliu
"""

import math

annual_salary = float(input("Enter your annual salary: "))
monthly_salary_og = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
semi_annual_raise += 1

total_cost = total_cost*0.25
current_savings = 0
r = 0.04
months = 0
monthly_salary = monthly_salary_og
        
while current_savings < total_cost:
    money_saved = monthly_salary*portion_saved   
    months +=1
    current_savings += current_savings*r/12 
    current_savings += money_saved
    monthly_salary = monthly_salary_og*(semi_annual_raise**math.floor(((months)/6)))

print("Number of months:", months)
