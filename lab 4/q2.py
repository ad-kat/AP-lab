import cmath
a=float(input("-->"))
b=float(input("-->"))
num=complex(a,b)

# Calculate sine value of the complex number
sine_value = cmath.sin(num)

# Calculate square root of the complex number
sqrt_value = cmath.sqrt(num)

# Calculate the natural logarithm (log) of the complex number
log_value = cmath.log(num)

# Print the results
print(f"Sine = = {sine_value}")
print(f"Sqrt = {sqrt_value}")
print(f"Natural log ={log_value}")


