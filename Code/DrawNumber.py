from LoadData import *
import numpy as np
import scipy.misc as smp

# Create a 28x28 matrix
z = 0
a = []

train_data = load_train_data()
def draw_number(array_of_number ):
    data = np.zeros((28,28), dtype=np.uint8)

    j = 0

    for i in range(len(array_of_number)):
        if((i%28 == 0) and (i != 0)):
            j += 1
        if((int(array_of_number[i]) < 255) and (int(array_of_number[i]) != 0)):
            array_of_number[i] = 255
        data[j,(i%28)] = array_of_number[i]
    img = smp.toimage( data )       # Create a PIL image
    img.show()
    exit(1)

print(len(train_data[2]))
draw_number(train_data[2][1:])


