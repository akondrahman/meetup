# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:01:00 2015

@author: User
"""



from multiprocessing import Process

def func1():
  print 'func1: starting'
  for i in xrange(10000000): pass
  print 'func1: finishing'
  return "oi mama oi"

def func2():
  print 'func2: starting'
  for i in xrange(10000000): pass
  print 'func2: finishing'
  return "kagu tumi koi"

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p1.join()
  p2.join()
   