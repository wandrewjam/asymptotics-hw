from sympy import *

e, x0, x1, x2 = symbols('e x0 x1 x2')
x = x0 + e*x1 + e**2*x2 + O(e**3)
f = e*x**3 - 3*x + 1
f = collect(expand(f),e)

print("\nFirst root\n")
eq0 = f.coeff(e,0)
print("Zeroth order:", solveset(eq0))
sol0 = Rational(1, 3)

x = x.subs(x0, sol0)
f = f.subs(x0, sol0)

eq1 = f.coeff(e,1)
print("First order:", solveset(eq1))
sol1 = Rational(1, 81)

x = x.subs(x1, sol1)
f = f.subs(x1, sol1)

eq2 = f.coeff(e, 2)
print("Second order:", solveset(eq2))
sol2 = Rational(1, 729)

x = x.subs(x2, sol2)
print("x = ", x)

y0, y1, y2 = symbols('y0 y1 y2')
y = y0 + e*y1 + e**2*y2 + O(e**3)
f = y**3 - 3*y + e
f = collect(expand(f), e)

print("\nSecond Root\n")
eq0 = f.coeff(e,0)
print("Zeroth order:", solveset(eq0))
sol0 = sqrt(3)

y = y.subs(y0, sol0)
f = f.subs(y0, sol0)

eq1 = f.coeff(e, 1)
print("First order:", solveset(eq1))
sol1 = Rational(-1, 6)

y = y.subs(y1, sol1)
f = f.subs(y1, sol1)

eq2 = f.coeff(e, 2)
print("Second order:", solveset(eq2))
sol2 = -sqrt(3)/Integer(72)

y = y.subs(y2, sol2)
x = collect(expand(y/e), e)
print("x =", x)

print("\nThird Root\n")
y = y0 + e*y1 + e**2*y2 + O(e**3)
f = y**3 - 3*y + e
f = collect(expand(f), e)

eq0 = f.coeff(e,0)
print("Zeroth order:", solveset(eq0))
sol0 = -sqrt(3)

y = y.subs(y0, sol0)
f = f.subs(y0, sol0)

eq1 = f.coeff(e, 1)
print("First order:", solveset(eq1))
sol1 = Rational(-1, 6)

y = y.subs(y1, sol1)
f = f.subs(y1, sol1)

eq2 = f.coeff(e, 2)
print("Second order:", solveset(eq2))
sol2 = sqrt(3)/Integer(72)

y = y.subs(y2, sol2)
x = collect(expand(y/e), e)
print("x =", x)
print("\n")
