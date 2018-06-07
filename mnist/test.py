import os, sys
import math

if __name__ == '__main__':
  index = 0
  for i in range(3, 10):
    base_learning_rate = 0.01
    while base_learning_rate <= 0.1:
      learning_decay_rate = 1
      while learning_decay_rate >= 0.5:
      	cmd = 'python3 convolutional.py --index ' + str(index) + ' --BATCH_SIZE ' + str(int(math.pow(2, i))) + ' --base_learning_rate ' + str(base_learning_rate) + ' --learning_decay_rate ' + str(learning_decay_rate)
        print(os.popen(cmd).read())
        index += 1
        learning_decay_rate -= 0.1
    base_learning_rate += 0.01