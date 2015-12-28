# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:04:06 2015

@author: User
"""



apiKey="267cf26785329627034706f15d2a5c"
import fetcher, utility
country="US"
radius=10 
#print "Sample run for getting meetup data"
#with  utility.duration(): 
#fetcher.sampleRun(apiKey, country, radius)
#print "Run for getting all meetup cities in USA"
#with  utility.duration(): 
#  output = fetcher.getCities(apiKey, country)
#  print "City output: ", output
  
#print "Run for getting all meetup categories"
#apiStrForCat="https://api.meetup.com/2/categories"
#with  utility.duration():
#  fetcher.getCategories(apiKey, apiStrForCat)
  #print "Category output: ", output
  


#print "Run for getting all meetup topics"
#apiStrForCat="https://api.meetup.com/topics"
#with  utility.duration():
#  fetcher.getTopics(apiKey, apiStrForCat)  

###################### Real work ! ########################
print "Run for getting all meetup events for a certain group"
apiStrForCat="https://api.meetup.com/find/groups"
country="US"
zipParam="27601"
categoryID=34
categoryName="Tech"
## for getting group info. 
with  utility.duration():
  groupDict = fetcher.getSpecificGroupInfo(categoryID, categoryName, country, zipParam, apiStrForCat, apiKey) 
  print "Group Dict info:", len(groupDict)
## for getting event info. based on groupID 
apiStrForEvent="https://api.meetup.com/2/events"  
with  utility.duration():
  for key_, val_ in groupDict.items():
    #print "val_", val_  
    groupIDOfInterest = key_
    groupURLNameOfInterest = val_[-1]    
    #print "Calling method with: {}, {}".format(groupIDOfInterest, groupURLNameOfInterest)
    eventDict = fetcher.getEventBasedOnGroup(groupIDOfInterest, 
                                             groupURLNameOfInterest, 
                                             apiStrForEvent, 
                                             apiKey )
    print "Detailed event dict info: ", len(eventDict)          
