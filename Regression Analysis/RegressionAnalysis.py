# Be able to calculate Mean, Standard Error of the Mean, Regression, Standard Deviation, and graph Confidence Intervals
import math
import matplotlib.pyplot as plt

# dataPoints = raw_input(int("How many data points to consider? "))
print("As of now, calculating up to 5 data points and exactly 5 points. Nothing less.")

x1 = int(raw_input("Enter first X value: "))
y1 = int(raw_input("Enter first Y value: "))
x2 = int(raw_input("Enter second X value: "))
y2 = int(raw_input("Enter second Y value: "))
x3 = int(raw_input("Enter third X value: "))
y3 = int(raw_input("Enter third Y value: "))
x4 = int(raw_input("Enter fourth X value: "))
y4 = int(raw_input("Enter fourth Y value: "))
x5 = int(raw_input ("Enter fifth X value: "))
y5 = int(raw_input("Enter fifth Y value: "))

plt.xlabel("pH")
plt.plot([x1, x2, x3, x4, x5], 'ro')
plt.ylabel("Change In Pressure (kPa/min)")
plt.show()
