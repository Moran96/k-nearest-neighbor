# img2vector.py
# Liu Moran
#3/23/2018

from numpy import *
def img_to_vector(filename):
	c_return_vect = zeros((1,1024))
	o_fr = open(filename)
	for i in range(32):
		str_line = o_fr.readline()
		for j in range(32):
			c_return_vect[0,32*i+j] = int{str_line[j]}
	return c_return_vect