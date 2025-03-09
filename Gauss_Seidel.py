# There is 1 limitation of this code that you will need to manually change the sign of the equations as per the equations given.
# I can fix this, but I have absolutely no time in my hands man !!


def gaussSiedel(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    y = z = 0;
    for i in range(1, 4):
        x = (1 / a1) * (d1 - b1 * y - c1 * z)
        y = (1 / b2) * (d2 - a2 * x - c2 * z)
        z = (1 / c3) * (d3 - a3 * x - b3 * y)
        print(f"x{i} = {x}")
        print(f"y{i} = {y}")
        print(f"z{i} = {z}")
        print()


coeff = []
coeffAlpha = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2', 'a3', 'b3', 'c3', 'd3']
print("Enter all the coefficients in Gauss Siedel order: ")
for i in range(12):
    print(f"{coeffAlpha[i]} = ", end="")
    coeff.append(int(input()))
print()
gaussSiedel(coeff[0], coeff[1], coeff[2], coeff[3], coeff[4], coeff[5], coeff[6], coeff[7], coeff[8], coeff[9], coeff[10], coeff[11])
