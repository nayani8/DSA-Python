# ----------------------------------------------------------
# Problem Title: Basic Recursion (Head & Tail)
# ----------------------------------------------------------
# Problem Statement:
# ------------------
# Demonstrate the concept of recursion by printing numbers:
#   - From 1 to n using Head and Tail recursion
#   - From n to 1 using Head and Tail recursion
#
# Key Concept:
# ------------
# 1. Head Recursion  → Recursive call happens first, print after call.
# 2. Tail Recursion  → Print happens first, recursive call after.
# ----------------------------------------------------------

n = int(input("Enter number: "))

# 1 to n (Head Recursion)
def hrn(n):
    if n == 0:
        return
    hrn(n - 1)
    print(n)

print("--> 1 to n (Head Recursion):")
hrn(n)

# 1 to n (Tail Recursion)
def trn(i, n):
    if i > n:
        return
    print(i)
    trn(i + 1, n)

print("\n--> 1 to n (Tail Recursion):")
trn(1, n)

# n to 1 (Head Recursion)
def nhr(i, n):
    if i > n:
        return
    nhr(i + 1, n)
    print(i)

print("\n--> n to 1 (Head Recursion):")
nhr(1, n)

# n to 1 (Tail Recursion)
def ntr(n):
    if n == 0:
        return
    print(n)
    ntr(n - 1)

print("\n--> n to 1 (Tail Recursion):")
ntr(n)
