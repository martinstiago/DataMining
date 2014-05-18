#!/usr/bin/env python

def zero_rules (input_file, program):
  name, attributes, classes, data = read_file(input_file)
  print name, attributes, classes, data

def read_file(input_file):
  attributes = []
  classes = []
  final_data = []
  data = []
  data_values = []
  data_classes = []

  name = input_file.readline().rstrip('\n')

  for line in input_file:

    if line != '@dados\n':

      if(line.split(',')[1] == 'real\n'):
        attributes.append(line.split(',')[0])

      elif(line.split(',')[1] == 'nominal'):
        classes = line.split(',')[2:-1]
        classes.append(line.split(',')[-1].rstrip('\n'))

      else:
        data_values.append(line.split(',')[0:len(attributes)])
        data_classes.append(line.split(',')[len(attributes)].rstrip('\n'))

      for index, value in enumerate(data_classes):
        data.append([value, data_values[index]])


  return name, attributes, classes, data