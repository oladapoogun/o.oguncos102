def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, t):
    A = P * (1 + R / n) ** (n * t)
    return A

def annuity_plan(PMT, R, n, t):
    A = PMT * (((1 + R / n) ** (n * t) - 1) / (R / n))
    return A

# Example usage
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (in %): "))
T = float(input("Enter Time Period (years): "))

print("Simple Interest Amount:", simple_interest(P, R, T))

n = int(input("Enter Number of Times Interest is Compounded per Year: "))
print("Compound Interest Amount:", compound_interest(P, R / 100, n, T))

PMT = float(input("Enter Payment Amount per Period: "))
print("Annuity Plan Amount:", annuity_plan(PMT, R / 100, n, T))
