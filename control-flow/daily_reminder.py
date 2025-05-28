#!/usr/bin/env python

# A script that provides a customized reminder for a task

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#condition statements using match case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Action note
if time_bound == "yes":
    print(f"Reminder: '{message}' that requires immediate attention today!")
else:
    print(f"Note: '{message}'. Consider completing it when you have free time.")
