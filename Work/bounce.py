# bounce.py
#
# Exercise 1.5

height = 100.0
num_of_bounces = 10

for i in range(1,num_of_bounces+1):
    height = 3*height/5
    print(i, round(height,4))
    