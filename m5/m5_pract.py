# iter = 0
# while iter<5:
# 	count=0
# 	for ch in "Hello":
# 		count+=1
# 		if iteration%2 == :
# 			
x = 25
epsilon = 0.01
step = 0.01
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
        # print(guess)
    else:
    	break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
