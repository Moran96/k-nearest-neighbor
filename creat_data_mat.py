import random

def creat(x,y):
	fileopen = open("datingTestSet.txt",'w')
	for i in range(0,x):
		for j in range(0,y):
			f = random.uniform(0,10)
			s = str(f)
			fileopen.write(s + '\t')
			#print(x)
		fileopen.write('\n')
	fileopen.close()
	print("Finished.")

def main():
	in1 = int(input("input x..."));
	in2 = int(input("input y..."));
	creat(in1,in2)

main()