import yaml
import numpy as np
from matplotlib import pyplot


accuracy = []
accuracy_5 = []

#NUMBER OF EXECUTORS
exec_count = 2

remove_char = dict.fromkeys(map(ord, ',%'), None)

with open("femnist_logging", 'r') as stream:
	for line in stream:
		word_list = line.split()
		for i in range(len(word_list)):
			if word_list[i] == 'test_accuracy':
				accuracy.append(word_list[i+1].translate(remove_char))
				prev1 = word_list[i+1]
			if word_list[i] == 'test_5_accuracy':
				accuracy_5.append(word_list[i+1].translate(remove_char))

charted_acc = []
charted_acc_5 = []


acc_x = 0

for i in range(len(accuracy)):
	if i%exec_count != exec_count-1:
		acc_x += float(accuracy[i])
	else:
		acc_x += float(accuracy[i])
		charted_acc.append(acc_x/exec_count)
		acc_x = 0

acc5_x = 0

for j in range(len(accuracy_5)):
	if j%exec_count != exec_count-1:
		acc5_x += float(accuracy_5[j])
	else:
		acc5_x += float(accuracy_5[j])
		charted_acc_5.append(acc5_x/exec_count)
		acc5_x = 0
	
#print(type(charted_acc), type(charted_acc_5))
#print(charted_acc, charted_acc_5)

pyplot.title("Line graph")
pyplot.plot(charted_acc, 'r+')
pyplot.plot(charted_acc_5, 'g+')

pyplot.savefig('plot_accuracy.png', format='png')
pyplot.show()
