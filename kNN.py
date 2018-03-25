from numpy import *
import operator

#------------------------------------------------------
def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

#--------------------------------------------------------
#There are 4 input parameters:
#input vector X, training instance set, attribute vector and num of neighbors.

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)

	return sortedClassCount[0][0]

#--------------------------------------------------------
#This function is to solve the problems of data format.
#Input the filename in str.
#Output the matrix of training instance and class_label_vector.

def file_to_matrix(filename):
	import numpy as np
	fr = open(filename)
	lis_lines = fr.readlines()
	int_number_of_lines = len(lis_lines)
	mat_return = zeros((int_number_of_lines,3))
	class_label_vector = []
	index = 0

	for line in lis_lines:
		line = line.strip()
		lis_contain_str = line.split('\t')
		lis_contain_float = [float(i) for i in lis_contain_str] 
		arr_contain_float = np.array(lis_contain_float)
		mat_return[index,:] = arr_contain_float
		class_label_vector.append(int(lis_contain_float[-1]))
		index +=1
	print(lis_contain_float[-1],type(lis_contain_float[-1]))
	fr.close()
	return mat_return,class_label_vector