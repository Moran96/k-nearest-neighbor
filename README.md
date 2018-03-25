# k_Nearest_Neighbor

## kNN算法示例1

1. 配置环境  
将 *creat_data_mat.py* 和 *kNN.py* 文件置于同一目录下.  
在当前目录打开Terminal.  
2. 生成数据文件  
通过 *random.uniform()* 函数生成一个1000行3列的float数据文档*datingTestSet.txt*.   
其中x表示行数,y表示列数.注意输入整型数据.
```
$python3 creat_data_mat.py
input x:>>>1000
input y:>>>3
Finished.
```
3. 导入数据
```
a@adeMacBook-Pro:~/Desktop/WorkSpace/recognition/training_digitals|
⇒  python3
Python 3.6.4 |Anaconda custom (64-bit)| (default, Jan 16 2018, 12:04:33)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import kNN
>>> from numpy import *
>>> mat,lab = kNN.file_to_matrix("datingTest.txt")
```
简单查看数据内容
```
>>> mat
array([[5.4322064 , 3.35448315, 4.16062565],
       [4.71442987, 3.1293185 , 6.17915431],
       [2.93174362, 6.28332409, 3.26137232],
       ...,
       [6.38221251, 1.38195624, 0.28057026],
       [4.0277301 , 0.39520326, 7.36550549],
       [4.90930118, 4.92608928, 6.65611991]])
>>> lab[0:20]
[4, 6, 3, 7, 6, 3, 8, 7, 1, 4, 4, 6, 5, 3, 5, 3, 0, 9, 2, 1]
>>>
```
4. 创建散点图
```
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111)
>>> ax.scatter(mat[:,1],mat[:,2])
<matplotlib.collections.PathCollection object at 0x10a535b38>
>>> plt.show()
```
若将散点图按照labels分类选取不同颜色,则可更改测试代码:   
```
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111)
>>> ax.scatter(mat[:,1],mat[:,2],15.0*array[lab],15.0*array[lab])
>>> plt.show()
```
