import numpy as np
import os
import cv2


def rescale(image, perc):
    perc = int(perc)
    if perc > 100:
        perc //= 100
        image1 = image.repeat(perc, 0).repeat(perc, 1)
    elif perc == 100:
        image1 = image
    else:
        perc = 100 // perc
        image1 = list()
        for i in range(len(image)):
            if i % perc == 0:
                image1.append(np.array([image[i, j] for j in range(len(image[0])) if j % perc == 0]))
    return np.array(image1)
    
    

def encoder(filename, count):
	a = cv2.imread(filename)
	#print(a.shape)
	row = 300
	col = 300
	try:
		a = cv2.resize(a, (col, row))
	except:
			a = rescale(a, 75)
			a = cv2.resize(a, (col, row))
	a = a.astype('str').reshape(row * col * 3)
	a = ':'.join(a)
	a = str(count) + "/" + a + '\n'
	with open('cars.txt', 'a') as f:
		f.write(a)
	#a = cv2.imread(filename)
	#cv2.imwrite('ccbd_images/' + str(count) + '.jpg', a)


count = 1
for i in os.listdir("cars_final"):
	print(count, i)
	encoder("ccbd_images/" + i, count)
	count += 1
