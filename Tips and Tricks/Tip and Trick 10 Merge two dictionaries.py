# Tip and Trick 10: Merge two dictionaries in a single expression

# For example, let say you have the following two dictionaries.

# currentEmployee = {1: "Scott", 2: "Eric", 3:"Kelly"}
# formerEmployee  = {2: "Eric", 4: "Emma"}

# And you want these two dictionaries merged. Let see how to do this.

currentEmployee = {1: "Scott", 2: "Eric", 3:"Kelly"}
formerEmployee  = {2: "Eric", 4: "Emma"}

allEmployee = {**currentEmployee, **formerEmployee}
print(allEmployee)

# Output:

# {1: 'Scott', 2: 'Eric', 3: 'Kelly', 4: 'Emma'}