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

## for getting event info. based on groupID 



def getMemberDetails(groupIDP, groupURLP):
    print "Executing 'getMemberDetails' "
  #with  utility.duration():    
    apiStrForMember="https://api.meetup.com/2/members"
    # let's get member info from each group: groupIDOfInterest, groupURLNameOfInterest     
    memberDict = fetcher.getMemberDetailsBasedOnGroup(groupIDP, groupURLP, apiStrForMember, apiKey) 
    print "Detailed member dict info: ", len(memberDict)          
    if (len(memberDict)>0): 
      print "Dumping member details in file ... ... ...", utility.dumpDictinFile(memberDict, "MemberDetails_", "output")    
    else:
      print "Wow ... no member for this group:", groupIDP  
    return memberDict      
    

def getEventDetails(groupIDP, groupURLP):
    print "Executing 'getEventDetails' "    
  #with  utility.duration():        
    apiStrForEvent ="https://api.meetup.com/2/events"      
    ## lets get event details for the group 
    eventDict = fetcher.getEventBasedOnGroup(groupIDOfInterest, 
                                             groupURLNameOfInterest, 
                                             apiStrForEvent, 
                                             apiKey )
    print "Detailed event dict info: ", len(eventDict)      
    if (len(eventDict)>0): 
      print "Dumping event details in file ... ... ...", utility.dumpDictinFile(eventDict, "EventDetails_", "output", "\t")
    else:
      print "Wow ... no event for this group:", groupIDP             
    return eventDict 


def getEventRatings(eventDictP):
  eventRatingDict={}
  print "Executing 'getEventRatings' "    
  #with  utility.duration():        
  apiStrForEventRating="https://api.meetup.com/2/event_ratings"
  #### code for event rating 
  for key_, val_ in eventDictP.items(): 
      eventID = key_   
      eventRatingDict = fetcher.getEventRating(eventID, 
                                             apiStrForEventRating, 
                                             apiKey )
      print "Event rating dict info: ", len(eventRatingDict)      
      if (len(eventRatingDict)>0): 
        print "Dumping event rating details in file ... ... ...", utility.dumpDictinFile(eventRatingDict, "EventRatings_", "output")      
      else:
        print "Wow ... no rating for this event:", eventID          
  #return eventRatingDict


def getEventComments(eventDictParam, groupIDParam):
  print "Executing 'getEventComments' "  
  #with  utility.duration():        
  #### code for event comments 
  apiStrForEventComments="https://api.meetup.com/2/event_comments"
  for key_, val_ in eventDictParam.items(): 
      eventID = key_   
      eventCommentDict = fetcher.getEventComment(eventID,
                                               groupIDParam,                                                   
                                               apiStrForEventComments, 
                                               apiKey )
      print "Event comment dict info: ", len( eventCommentDict )      
      if (len( eventCommentDict )>0): 
        print "Dumping event comments in file ... ... ...", utility.dumpDictinFile(eventCommentDict, "EventComments_", "output")           
      else:
        print "Wow ... no comments for this event:", eventID          
  #return eventCommentDict





def getOtherDetailsOfMember(memDictParam):
  print "Executing 'getOtherDetailsOfMember' "  
  #with  utility.duration():        
    #### code for other member details 
  for key_, val_ in memDictParam.items(): 
      memID = key_   
      apiStrForMemDetails="https://api.meetup.com/members/" + memID      
      otherMemDict = fetcher.getOtherMemberDetails(memID, apiStrForMemDetails, apiKey)
      print "Other membership dict info: ", len( otherMemDict )      
      if (len( otherMemDict )>0): 
        print "Dumping other membership info in file ... ... ...", utility.dumpDictinFile(otherMemDict, "OtherMembership_", "output")           
      else:
        print "Wow ... no other membership for this member:", memID          
  #return otherMemDict



###################### Real work ! ########################
print "Run for getting all meetup events for a certain group"
apiStrForCat="https://api.meetup.com/find/groups"
country="US"
zipParam="27601"
categoryID=34
categoryName="Tech"
groupDict={}
## for getting group info. 
with  utility.duration():
  groupDict = fetcher.getSpecificGroupInfo(categoryID, categoryName, country, zipParam, apiStrForCat, apiKey) 
  print "Group Dict info:", len(groupDict)
  for key_, val_ in groupDict.items():
    print "Executing the five methods ...."  
    groupIDOfInterest = key_
    groupURLNameOfInterest = val_[-1]    
    #print "Calling method with: {}, {}".format(groupIDOfInterest, groupURLNameOfInterest)
    ##### Method-1
    memDict          =  getMemberDetails(groupIDOfInterest, groupURLNameOfInterest)    
    ##### Method-2
    #eventDict        =  getEventDetails(groupIDOfInterest, groupURLNameOfInterest)
    ##### Method-3
    #getEventRatings(eventDict)
    ##### Method-4
    #getEventComments(eventDict, groupIDOfInterest)
    ##### Method-5
    getOtherDetailsOfMember(memDict)    





    












 