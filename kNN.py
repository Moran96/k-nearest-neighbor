from numpy import *
import operator

#------------------------------------------------------
def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

#----------------------------------------------------------------
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

#----------------------------------------------------------------
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

#----------------------------------------------------------------
#This function can change the data from (min,max) to (0,1).
#The new value of each data obey the rules:
#        new_value = (old_value - min)/(max-min)
#Input dataset;
#Output new dataset, ranges and min_values

def auto_norm(data_set):
	min_values = data_set.min(0)
	max_values = data_set.max(0)
	ranges = max_values - min_values
	norm_data_set = zeros(shape(data_set))
	m = data_set.shape[0]
	norm_data_set = data_set - tile(min_values,(m,1))
	norm_data_set = norm_data_set/tile(ranges,(m,1))

	return norm_data_set,ranges,min_values

#----------------------------------------------------------------
#
#
#Test

def dating_class_test():
	ho_ratio = 0.10
	dating_data_mat,dating_labels = file_to_matrix("datingTestSet.txt")
	norm_mat,ranges,min_values = auto_norm(dating_data_mat)
	m = norm_mat.shape[0]
	num_test_vecs = int(m*ho_ratio)
	error_count = 0.0

	for i in range(num_test_vecs):
		classifier_result = classify0(norm_mat[i,:],norm_mat[num_test_vecs:m,:],dating_labels[num_test_vecs:m],3)
		print("the classifier came back with: %d, the real answer is: %d" %(classifier_result,dating_labels[i]))

		if (classifier_result != dating_labels[i]):
			error_count +=1.0
	print("the total error rate is: %f" %(error_count/float(num_test_vecs)))

#-----------------------------------------------------------------------------
