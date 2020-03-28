import time
import csv
import os

DIR = '../default_detection_save_dir/'
'''
try:
    with open(DIR + 'test.csv')as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print('year={} mon={} day={} h={} m={} s={} detection={}'.format(
                row['year'],
                row['mon'],
                row['day'],
                row['h'],
                row['m'],
                row['s'],
                row['detection']
            ))
except:
    print('test.csvが無かったね')
'''
with open(DIR + 'test.csv','a')as csvfile:
    fieldnames=['year','mon','day','h','m','s','detection']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'year':2020,'mon':3,'day':20,'h':0,'m':1,'s':2,'detection':'test'})