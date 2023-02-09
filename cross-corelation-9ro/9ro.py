import numpy as np
loc = np.array([[1, 5, 9], [3, 7, 11]])
for y, x in sorted(zip(loc[0], loc[1])):
print("y:", y, "x:", x)