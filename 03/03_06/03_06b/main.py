employee_salaries = {
  "Alice": 50000,
  "Bob": 60000
}

# print(employee_salaries["Charlie"])
print(employee_salaries.get("Charlie"))

# try-except
try:
  charlie_salary = employee_salaries["Charlie"]
except KeyError:
  print("Charlie is still not found")