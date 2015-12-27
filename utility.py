# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:06:55 2015

@author: User
"""



from contextlib import contextmanager
@contextmanager
def duration():
  import time  
  t1 = time.time()
  yield
  t2 = time.time()
  print("\n" + "-" * 72)
  print("# Runtime: %.3f secs" % (t2-t1)) 