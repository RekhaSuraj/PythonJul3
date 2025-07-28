# control flow statements
# In Python, continue, break, and pass are control flow statements used in loops and
# conditional statements, but they behave differently:

# 1. break
# Exits the loop completely.

# The execution resumes at the first statement after the loop.
for i in range(5):
    if i == 3:
        break

    print(i)

print('Outside of loop')

# 0
# 1
# 2
# Outside of loop

print()
# 2. continue
# Skips the current iteration and moves to the next iteration of the loop
for i in range(5):
    if i == 3:
        continue

    print(i)

print('Outside of loop')

# 0
# 1
# 2
# 4
# Outside of loop

# 3. pass
# Does nothing : It is a placeholder where a statement is syntactically required but not implemented yet

class Login:

    def login_admin(self):
        pass  # Placeholder for future code


class Checkout:
    pass


class Listing:
    ...


for i in range(10):
    pass


# Statement	Function
# break		Exits the loop entirely
# continue	Skips the current iteration and continues to the next
# pass		Does nothing, acts as a placeholder