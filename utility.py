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
  
def dumpEventsinFile(eventDictParam, fileParam, dirParam, delimiter=","):
  import os   
  completeStrToWrite=""
  if not os.path.exists(dirParam):
    os.makedirs(dirParam)  
  fileParam = dirParam + "/" + fileParam + ".csv"
  fileToWrite = open( fileParam, 'a')
  lineStr = "" 
  #lineStr =  "EventID" +","  + "Name" + ","  + "Status" +"," + "Visibility" +"," 
  #lineStr =  lineStr   + "URL" +","  + "Duration" +"," + "Desc." +"," + "Address" +"," 
  #lineStr =  lineStr   + "City" +","  + "RSVPLimit" +","  + "YesCount" +"," 
  #lineStr =  lineStr   + "GroupID" +"," + "GroupURL" +","
  fileToWrite.write(lineStr + "\n") 
  for key, values in eventDictParam.items():
    lineStr = str(key) + delimiter  
    for item in values:    
        lineStr = lineStr + str(item) + delimiter
    lineStr = lineStr + "\n"  
    completeStrToWrite = completeStrToWrite + lineStr  
    lineStr=""
  fileToWrite.write(completeStrToWrite );
  fileToWrite.close()
  return "Done ... D-U-M-P-I-N-G!"    
  