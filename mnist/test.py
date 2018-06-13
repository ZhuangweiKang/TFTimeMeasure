# encoding: utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import sys
import math
import csv

if __name__ == '__main__':
  with open('test_result.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Test_id', 'Batchsize', 'Base_learning_rate', 'Learning_decay_rate', 'Dropout_rate', 'Total_learning_time', 'Test_error'])

  index = 0
  for i in range(10, 2, -1):
    base_learning_rate = 0.01
    while base_learning_rate <= 0.1:
      learning_decay_rate = 1
      while learning_decay_rate >= 0.5:
        dropout_rate = 0.5
        while dropout_rate >= 0:
          print('Index: %d' % index)
          print('Batch Size: %d' % int(math.pow(2, i)))
          print('Base learning rate: %f' % base_learning_rate)
          print('Learning decay rate: %f' % learning_decay_rate)
          print('Dropout rate: %f ' % dropout_rate)
          cmd = 'python convolutional.py --index ' + str(index) + ' --BATCH_SIZE ' + str(int(math.pow(2, i))) + ' --base_learning_rate ' + str(base_learning_rate) + ' --learning_decay_rate ' + str(learning_decay_rate) +' --dropout_rate ' + str(dropout_rate)
          print(os.popen(cmd).read())
          dropout_rate -= 0.1
          index += 1
        learning_decay_rate -= 0.1
    base_learning_rate += 0.01
