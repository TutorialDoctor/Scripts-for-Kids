# Fuzzy Logic - By the Tutorial Doctor
# December 24, 2021

# Five kids are standing against a wall from shortest to tallest. Here are the heights of the kids in feet:
import random

kid_heights = [4.34,5.4,5.5,6.0,6.1]

# Which of the kids are short and which ones are tall? To answer this, you might create a rule:

for height in kid_heights:
	if height < 5:
		print("short")
	else:
		print("tall")

# Is this accurate? What if a kid was exactly 5 feet or 4.999 feet, would they still be considered short? Using a range isn't any better:

for height in kid_heights:
	if height in range(0,5):
		print("short")
	else:
		print("tall")

# As you can see, it is hard to represent the classification of tall or short kids with crisp values and boolean logic. Height is relative, as is many other things. Height, when speaking of kids, is different from height when speaking of mountains.

# Instead of representing a kid as short or tall, it's better to represent a kid as having a degree of "tallness" or "shortness". A kid should be either 0% tall or 100% tall or 50% tall. "Tallness" and "shortness" are fuzzy terms that can be represented using fuzzy logic. If a kid is 90% tall, they could be considered 10% short. For now we wont't factor in that they could also be another % average height.

# The best way to represent the heights of the kids is to represent their "tallness" as a percentage of their height between a shortest height and a tallest height. This percentage lets you know how much of a member the kid is to the classification of "tall". A function that tells you the membership of a value is called a membership function.

shortest_height = 3.5
tallest_height = 6.1
height_range = [shortest_height,tallest_height]

def Membership(value,List):
	"Returns the membership of a value in a list."
	top = float(value) - List[0] #input value minus the first value in the range
	bottom = List[1] - List[0] # last range value minus the first range value
	M = top/bottom
	return M

# Now we can get the percentage of tallness of a kid in a range heights

for height in kid_heights:
	print(Membership(height,height_range))

# Now let's choose some random values to represent average height. Values above 1.0 are above average and negative values are below average. Both above-average and below-average heights are not in the range of average heights, but they still have a degree of membership to the average height range

print("Average Height")

average_height = [4.35,5.5]

for height in kid_heights:
	print(Membership(height,average_height))

# This works for temperatures as well.

print("Temperatures")
temperatures = [-1, 30, 90, 45, 10]
hot = [85,109]
cold = [-20,50]

print("Hotness")
for temperature in temperatures:
	print(Membership(temperature,hot))

print("Coldness")
for temperature in temperatures:
	print(Membership(temperature,cold))

# The interesting thing about this is that we can use the membership of a value to one range to drive or affect some other system. 

torque = 0
print("Torque")

for temperature in temperatures:
	torque = 1 + (torque * Membership(temperature,hot))
	new_torque = torque
print(new_torque)

# Notice that making one of the temperatures extremely high has an affect on the torque.
	
# Below is a neat little function:
	
def Is(x,List):
	"Returns true if a value is in the value range of a list"
	if Membership(x,List) < 0:
		print("not a member of the list")
		return False
	#If a value is greater than the first item in a list..
	if x >= List[0]:
		#And if it is smaller than the last item in the list...
		if x<= List[1]:
			#print the membership of the item in the list...
			#print(str(x) + " is " + str(Membership(x,List)) + " percent " + List[2])
			print(f'{str(x)} is {Membership(x,List)} percent {List[2]}')
			#And return True
			return True
	#No else statement is needed since the return statement will exit the function.
	#Print the membership and return False if the above condition is false.
	print(f'{str(x)} is {Membership(x,List)} percent {List[2]}')
	return False 

tall = [0,100,'tall']
Is(4,tall)

funny = [1,5,'funny']
Is(4,funny)

# The American Conference of Governmental Industrial Hygienists (ACGIH) recommends an 8- hour TWA Threshold Limit Value (TLV) of 5,000 ppm and a Ceiling exposure limit (not to be exceeded) of 30,000 ppm for a 10-minute period. A value of 40,000 is considered immediately dangerous to life and health (IDLH value).

dangerous = [5000,30000,'dangerous level']
Is(40000,dangerous)

life_threatening = [30000,40000,'life threatening']
Is(35000,life_threatening) # 50/50 chance you will die (well, we should use probability here)

print("randoms")
random_heights = []
for x in range(0,len(kid_heights)):
	random_heights.append(random.uniform(0,kid_heights[-1]))
	
print(random_heights)

# Lets see a graph (because we all like graphs, right?

import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')


plt.style = 'ggplot'
plt.xkcd()

#plt.animated = True

def range_float(start,stop,step):
	x = start
	while x <= stop:
		yield x
		x = x + step
rf = range_float(start=shortest_height,stop=tallest_height,step=1)
base = [x for x in rf]
print(base)

nparr = np.array(kid_heights)
thickness = 3

#plt.plot(base,color="#E35EE4",label="Membership")
axs[0].plot([h for h in kid_heights if h < 5.5],label="< 5.5",linewidth=5,color="green")

#plt.plot([h for h in kid_heights if h >= average_height[0] and h <= average_height[1]],label="< 5.5",linewidth=5)

#print([x for x in range_float(average_height[0],average_height[1],.1)])

average_kids = [kid_heights[0]]+[h for h in kid_heights if h > average_height[0] and h < average_height[1]]
axs[0].plot(average_kids,label = "average")

print(average_kids)
#plt.plot([x*tallest_height for x in [tallest_height-tallest_height,shortest_height]])

print(base)

axs[0].plot(nparr, color='#444444', linestyle='--' ,label="kid hegts", marker='o')
axs[1].plot(random_heights, color='orange', linestyle='--' ,label="random", marker='o')
#plt.plot(np.array(average_height),color='#5a7d9a',label="Average", marker='o',linewidth=thickness)

axs[0].set_xlabel("Kids")
axs[0].set_ylabel("Heights")
axs[1].set_ylabel("Random Heights")
axs[0].set_title("kid Heights")
axs[0].legend(loc=0) #0 is best
axs[1].legend(loc=0) #0 is best
#plt.gca().xaxis.label.set_size(5)
axs[0].grid()
#plt.tight_layout()

#plt.savefig("plot.png")
axs[0].set_xticks(np.arange(0, len(kid_heights)+1, step=1),)
axs[0].set_xticklabels(['1st','2nd','3rd','4th','5th','6th'])
#plt.yticks(np.arange(0, len(kid_heights), step=1),kid_heights)
plt.gca().xaxis.label.set_color('red')
plt.gca().yaxis.label.set_color('blue')

def truncated_float(f):
	return float("{:.2f}".format(f))

for x, y in zip(kid_heights, list(range(0,len(kid_heights)))):
    axs[0].text(y, x, str(x)+ " " +str(Membership(x,kid_heights)), color="red", fontsize=12)

for x, y in zip(random_heights, list(range(0,len(random_heights)))):
    plt.text(y, x, str(truncated_float(x)), color="pink", fontsize=12)
    
plt.show()

# Some good resources I found after writing this:
#https://youtu.be/UO98lJQ3QGI
# https://web.pdx.edu/~nauna/week7-final.pdf

