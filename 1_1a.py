"""
Finds the asymptotic expansions of the three roots of 
  the polynomial e*x^3 - 3*x + 1 = 0 where e << 1
"""

from sympy import *

# Define symbols, expansion of x, and the function
e, x0, x1, x2 = symbols('e x0 x1 x2')
x = x0 + e*x1 + e**2*x2 + O(e**3)
f = e*x**3 - 3*x + 1

# Write f as a power series in e
f = collect(expand(f),e)

# Set the O(1) terms equal to 0, and output result
print("\nFirst root\n")
eq0 = f.coeff(e,0)
print("Zeroth order:", solveset(eq0))
sol0 = Rational(1, 3) # Solution for x0

# Substitute the solution into x0
x = x.subs(x0, sol0) # In the expansion of x
f = f.subs(x0, sol0) # and in the expansion of f

# Set the O(e) terms equal to 0, and output result
eq1 = f.coeff(e,1)
print("First order:", solveset(eq1))
sol1 = Rational(1, 81) # Solution for x1

# Substitute the solution into x1
x = x.subs(x1, sol1)
f = f.subs(x1, sol1)

# Set the O(e^2) terms equal to 0, and output result
eq2 = f.coeff(e, 2)
print("Second order:", solveset(eq2))
sol2 = Rational(1, 729) # Solution for x2

#Substitute the solution into x2 and output x
x = x.subs(x2, sol2)
print("x = ", x)

# Change of variables to reveal the solutions near infinity
# The change of variables is x = y/sqrt(e)
# Define new variable y, and the rescaled equation f
# NOTE: e is redefined below this point:
#       e_below := sqrt(e_above)
y0, y1, y2 = symbols('y0 y1 y2')
y = y0 + e*y1 + e**2*y2 + O(e**3)
f = y**3 - 3*y + e

# Write f as a power series in e
f = collect(expand(f), e)

# Set the O(1) terms equal to 0, and output result
print("\nSecond Root\n")
eq0 = f.coeff(e,0)

# There are three solutions to the leading order problem:
# 0 is a trivial solution, and the other two are relevant
print("Zeroth order:", solveset(eq0)) 
sol0 = sqrt(3) # Pick one of the relevant roots

# Substitute the solution into y0
y = y.subs(y0, sol0)
f = f.subs(y0, sol0)

# Set the O(e) terms equal to 0, and output result
eq1 = f.coeff(e, 1)
print("First order:", solveset(eq1))
sol1 = Rational(-1, 6) # Solution for y1

# Substitute the solution into y1
y = y.subs(y1, sol1)
f = f.subs(y1, sol1)

# Set the O(e^2) terms equal to 0, and output result
eq2 = f.coeff(e, 2)
print("Second order:", solveset(eq2))
sol2 = -sqrt(3)/Integer(72) # Solution for y2

# Substitute the solution into y2, and change variables back to original
y = y.subs(y2, sol2)
x = collect(expand(y/e), e)
print("x =", x)

# Using the same change of variables as for the second root
# Redefine expansion of y, and rescaled equation f
print("\nThird Root\n")
y = y0 + e*y1 + e**2*y2 + O(e**3)
f = y**3 - 3*y + e

# Collect terms in powers of e
f = collect(expand(f), e)

# Set the O(1) terms equal to 0, and output result
eq0 = f.coeff(e,0)
print("Zeroth order:", solveset(eq0))
sol0 = -sqrt(3) # Now use the other relevant root for y0

# Substitute the solution into y0
y = y.subs(y0, sol0)
f = f.subs(y0, sol0)

# Set the O(e) terms equal to 0, and output result
eq1 = f.coeff(e, 1)
print("First order:", solveset(eq1))
sol1 = Rational(-1, 6) # Solution for y1

# Substitute the solution into y1
y = y.subs(y1, sol1)
f = f.subs(y1, sol1)

# Set the O(e^2) terms equal to 0, and output result
eq2 = f.coeff(e, 2)
print("Second order:", solveset(eq2))
sol2 = sqrt(3)/Integer(72) # Solution for y2

# Substitute the solution into y2, and change variables back to original
y = y.subs(y2, sol2)
x = collect(expand(y/e), e)
print("x =", x)
print("\n")
