import numpy as np
from os import listdir
import operator
import sys

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def numberV(filename):
	result = np.zeros((1, 1024))
	with open(filename) as f:
		for i in range(32):
			line = f.readline()
			for j in range(32):
				result[0, 32 * i + j] = int(line[j])
	return result

training = sys.argv[1]
test = sys.argv[2]
labels = []
trainingFile = listdir(training)
trainingLength = len(trainingFile)
trainingMat = np.zeros((trainingLength, 1024))
for i in range(trainingLength):
	filename = trainingFile[i]
	fileF = filename.split('.')[0]
	number = int(fileF.split('_')[0])
	labels.append(number)
	trainingMat[i, :] = numberV("{}/{}".format(training, filename))

errorNum = 0
testFile = listdir(test)
testLength = len(testFile)
for i in range(20):
	errorNum = 0
	for j in range(testLength):
		filename = testFile[j]
		fileF = filename.split('.')[0]
		number = int(fileF.split('_')[0])
		classifyResult = classify0(numberV("{}/{}".format(test, filename)), trainingMat, labels, i+1)
		if classifyResult != number:
			errorNum += 1
		error = (errorNum / testLength) * 100
	print(int(error))
