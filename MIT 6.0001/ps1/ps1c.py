# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:09:36 2022

@author: setonliu
"""

import math

annual_salary = float(input("Enter your annual salary: "))
monthly_salary_og = annual_salary/12
semi_annual_raise = 1.07

total_cost = 1000000*0.25
current_savings = 0
r = 0.04
        

monthly_salary = monthly_salary_og

money_saved = monthly_salary
for months in range(36):
    money_saved = monthly_salary   
    months +=1
    current_savings += current_savings*r/12 
    current_savings += money_saved
    monthly_salary = monthly_salary_og*(semi_annual_raise**math.floor(((months)/6)))

if current_savings < total_cost:
    print("It is not possible to pay the down payment in three years.")
else:
    current_savings = 0
    low = 0
    high = 10000
    mid = (low+high)/2
    monthly_salary = monthly_salary_og
    
    counter = abs(current_savings-total_cost)
    steps = 0
    
    while counter > 100:
        for months in range(36):
            percent =float(mid)/float(10000)
            #percent = 0.4411
            money_saved = monthly_salary*percent
            current_savings += current_savings*r/12 
            current_savings += money_saved
            monthly_salary = monthly_salary_og*(semi_annual_raise**math.floor(((months+1)/6)))
        if current_savings < total_cost:
            low = mid
        if current_savings > total_cost:
            high = mid
        mid = (low+high)/2
        counter = abs(current_savings-total_cost)
        current_savings = 0
        monthly_salary = monthly_salary_og
        money_saved = 0
        steps += 1
    
    print("Best savings rate:", percent)
    print("Steps in bisection search:", steps)


    