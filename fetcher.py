# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:14:45 2015

@author: User
"""



from __future__ import unicode_literals
import time 
import codecs
import sys

def sampleRun(apiKeyParam, countryParam, radiusParam=10):


  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  ## final output holder 
  #resultStr=""  
  ## set up the cities 
  cities =[("Bridgeport","CT"),("New Haven","CT"),("Hartford","CT"),("Stamford","CT"),("Waterbury","CT")]


  for (city, state) in cities:
            per_page = 200
            results_we_got = per_page
            offset = 0
            while (results_we_got == per_page):
                # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
                response=get_results({"sign":"true","country":countryParam, 
                                      "city":city, "state":state, "radius": radiusParam, 
                                      "key":apiKeyParam, "page":per_page, "offset":offset })
                                 
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    category = ""
                    if "category" in group:
                        category = group['category']['name']
                    print "," .join(map(unicode, [city, 
                                                  group['name'].replace(","," "), 
                                                  group['created'], group['city'], group.get('state',""), category, group['members'], 
                                                  group.get('who',"").replace(","," ")]))
                    #print resultStr
            time.sleep(1)
            
            
def queryForCities(paramList):
  import requests   
  request = requests.get("https://api.meetup.com/2/cities",params=paramList)
  #print "Cities: request string: ", request
  data = request.json()
  return data    


def get_results(params):
  import requests   
  request = requests.get("http://api.meetup.com/2/groups",params=params)
  #print "Sample run: request string: ", request  
  data = request.json()
  return data





def execQuery(queryParam, apiParam):
  import requests   
  requestHolder = requests.get(apiParam,params=queryParam)
  valToRet = requestHolder.json()
  return valToRet  

            
def getCities(apiKeyParam, countryParam):


  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  ## final output holder 
  #resultStr= "," +  "City," + "State," + "Country," + "Zip," + "\n"
  ## set up the cities 
  #cities =[("Bridgeport","CT"),("New Haven","CT"),("Hartford","CT"),("Stamford","CT"),("Waterbury","CT")]

  per_page = 200
  results_we_got = per_page
  offset = 0
  while (results_we_got == per_page):
                response=queryForCities({"sign":"true", "photo-host":"public", "country":countryParam, 
                                      "key":apiKeyParam, "page":per_page, "offset":offset })
                ### response has the results for for the corresponding query 
                ## sanity checking                       
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    tempResHolder = map(unicode, [group['id'], group['city'], group['state'], group['country'], group['zip'], group['ranking']])
                    print "," .join(tempResHolder)
                    #print resultStr
                    #for strI in tempResHolder:
                    #  resultStr = resultStr + strI + ","    
                    #resultStr= resultStr +  "\n"
  time.sleep(1)          
  #return resultStr  
  

def getCategories(apiKeyParam, apiStringP):
  #https://api.meetup.com/2/categories?offset=0&sign=True&format=json&photo-host=public&page=20&order=shortname&desc=false      

  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  ## final output holder 
  #resultStr= "," +  "ID," + "Name," + "Shortname," + "\n"


  per_page = 200
  results_we_got = per_page
  offset = 0
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                      "key":apiKeyParam, "page":per_page, "offset":offset }, apiStringP)
                ### response has the results for for the corresponding query 

                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    print "," .join(map(unicode, [group['id'], group['name'], group['shortname']]))

  time.sleep(1)     


def getTopics(apiKeyParam, apiStringP):
  #https://api.meetup.com/topics?&sign=true&photo-host=public&page=20


  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  per_page = 200
  results_we_got = per_page
  offset = 0
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                      "key":apiKeyParam, "page":per_page, "offset":offset }, apiStringP)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    print "," .join(map(unicode, [group['id'], group['name'], group['members']]))

  time.sleep(1)     
  
  
  
def getSpecificGroupInfo(catIDP, catNameP, countryP, zipP, apiStringP, apiKeyP):
#https://api.meetup.com/find/groups?&sign=true&photo-host=public&zip=27601&country=US&page=20    
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")

  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  per_page = 200
  results_we_got = per_page
  offset = 0
  resCounter =  1
  ## the final dictionary 
  dictToRet={}
  #headerList=["GroupID", "GroupName", "GroupMemberCount", "GroupURL"]
  #print "\t" .join(headerList)
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                      "zip":zipP, "key":apiKeyP, "page":per_page, "offset":offset }, apiStringP)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                results_we_got = len(response)
                
                for cnt in xrange(per_page):

                  #print "debugging stuff: response length{}, current count ={}".format(len(response), cnt)
                  if cnt < len(response):
                    if 'category' in response[cnt]: 
                      group_category_name = response[cnt]['category']['name']
                      group_category_id   = response[cnt]['category']['id']
                      if ((group_category_id==catIDP) and (group_category_name==catNameP)):
                        #print "results inside stuff ... ", response[cnt]  
                        content = map(unicode, [resCounter, cnt, response[cnt]['id'], response[cnt]['name'], 
                           response[cnt]['members'], response[cnt]['urlname'], response[cnt]['visibility']])
                        #print "inside content: ", content   
                        decoded_content = [x.decode('utf-8').strip() for x in content]                  
                      
                        #print "\t" .join(decoded_content)
                        ## group IDs are numeric so far 
                        dictToRet[int(decoded_content[2])] = [decoded_content[6], decoded_content[3], decoded_content[4], decoded_content[5]]
                        resCounter += 1   

  time.sleep(1)  
  return dictToRet



def getEventBasedOnGroup(groupIDP, groupURLNameOfInterestP, apiStringP, apiKeyP):
  #https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=Raleigh-Nerd-Herd&group_id=3040382&page=20    
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")

  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  per_page = 200
  results_we_got = per_page
  offset = 0
  resCounter =  1
  ## the final dictionary 
  dictToRet={}
  #headerList=["EventID", "EventName", "EventStatus", "Visibility", "EventURL", "EventDuration"]
  #print "\t" .join(headerList)
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                      "group_urlname":groupURLNameOfInterestP, "group_id": groupIDP,  
                                      "key":apiKeyP, "page":per_page, "offset":offset }, apiStringP)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                
                for evtItem in response['results']:
                    if 'duration' in evtItem:
                      durString= evtItem['duration'] 
                    else:
                      durString="00000000"  
                    if 'rsvp_limit' in evtItem:
                      rsvpLimitString= evtItem['rsvp_limit'] 
                    else:
                      rsvpLimitString= "Unknown"  
                    if 'yes_rsvp_count' in evtItem:
                      yesrsvpCountString= evtItem['yes_rsvp_count'] 
                    else:
                      yesrsvpCountString= "Unknown"  
                    if 'venue' in evtItem:
                      addrString = evtItem['venue']['address_1'] 
                      cityString = evtItem['venue']['city']
                    else:
                      addrString = "UNKNOWN" 
                      cityString = "UNKNOWN"
                    if 'description' in evtItem:
                      descString = evtItem['description']
                    else:
                      descString = "Not Given"
                    content = map(unicode, [
                                            evtItem['id'], evtItem['name'], 
                                            evtItem['status'], evtItem['visibility'], 
                                            evtItem['event_url'], durString,
                                            descString , addrString, 
                                            cityString , rsvpLimitString, yesrsvpCountString,       
                                            groupIDP ,  groupURLNameOfInterestP
                                           ]
                                 )
                    
                    decoded_content = [x.decode('utf-8').strip() for x in content]                  
                    #print "\t" .join(decoded_content)
                    dictToRet[decoded_content[0]] = [
                                                     decoded_content[1], decoded_content[2], 
                                                     decoded_content[3], decoded_content[4], 
                                                     decoded_content[5], decoded_content[6], 
                                                     decoded_content[7], decoded_content[8], 
                                                     decoded_content[9], decoded_content[10], 
                                                     decoded_content[11], decoded_content[12]
                                                    ]
                    resCounter += 1   

  time.sleep(1)  
  return dictToRet     
  
  
def getMemberDetailsBasedOnGroup(groupIDP, groupURLNameOfInterestP, apiStringP, apiKeyP):
  #https://api.meetup.com/2/members?&sign=true&photo-host=public&group_urlname=TRINUG&group_id=2235051&page=20
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")

  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  per_page = 200
  results_we_got = per_page
  offset = 0
  resCounter =  1
  ## the final dictionary 
  dictToRet={}
  #headerList=["EventID", "EventName", "EventStatus", "Visibility", "EventURL", "EventDuration"]
  #print "\t" .join(headerList)
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                      "group_urlname":groupURLNameOfInterestP, "group_id": groupIDP,  
                                      "key":apiKeyP, "page":per_page, "offset":offset }, apiStringP)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                
                for evtItem in response['results']:
                    if 'country' in evtItem:
                      countryString= evtItem['country'] 
                    else:
                      countryString="Unknown"  
                    if 'city' in evtItem:
                      cityString= evtItem['city'] 
                    else:
                      cityString= "Unknown"  
                    if 'state' in evtItem:
                      stateString= evtItem['state'] 
                    else:
                      stateString= "Unknown"  
                    if 'id' in evtItem:
                      IDString = evtItem['id']
                    else:
                      IDString = "Unknown"
                    if 'name' in evtItem:
                      nameString = evtItem['name']
                    else:
                      nameString = "Not Given"
                    if 'status' in evtItem:
                      statusString = evtItem['status']
                    else:
                      statusString = "Not Given"
                    content = map(unicode, [
                                            IDString, nameString, 
                                            statusString, cityString, 
                                            stateString, countryString, 
                                            groupIDP ,  groupURLNameOfInterestP
                                           ]
                                 )
                    
                    decoded_content = [x.decode('utf-8').strip() for x in content]                  
                    #print "\t" .join(decoded_content)
                    dictToRet[decoded_content[0]] = [
                                                     decoded_content[1], decoded_content[2], 
                                                     decoded_content[3], decoded_content[4], 
                                                     decoded_content[5], decoded_content[6], 
                                                     decoded_content[7]
                                                    ]
                    resCounter += 1   

  time.sleep(1)  
  return dictToRet
def getEventRating(eventID, apiStrForEvent, apiKey ):
  # https://api.meetup.com/2/event_ratings?&sign=true&photo-host=public&event_id=1300571&page=20  
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")

  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  per_page = 200
  results_we_got = per_page
  offset = 0
  resCounter =  1
  ## the final dictionary 
  dictToRet={}
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                    "event_id": eventID,  
                                    "key":apiKey, "page":per_page, "offset":offset }, apiStrForEvent)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                
                for evtItem in response['results']:
                    if 'event_id' in evtItem:
                      eventIDString= evtItem['event_id'] 
                    else:
                      eventIDString ="Unknown"  
                    if 'member_id' in evtItem:
                      memIDString= evtItem['member_id'] 
                    else:
                      memIDString= "Unknown"  
                    if 'member_name' in evtItem:
                      memNameString= evtItem['member_name'] 
                    else:
                      memNameString= "Unknown"  
                    if 'rating' in evtItem:
                      ratingString = evtItem['rating']
                    else:
                      ratingString = "Unknown"
                    content = map(unicode, [
                                            eventIDString , memIDString, 
                                            memNameString, ratingString 
                                           ]
                                 )
                    
                    decoded_content = [x.decode('utf-8').strip() for x in content]                  
                    #print "\t" .join(decoded_content)
                    dictToRet[decoded_content[0]] = [
                                                     decoded_content[1], decoded_content[2], 
                                                     decoded_content[3] 
                                                    ]
                    resCounter += 1   

  time.sleep(1)  
  return dictToRet     




def getEventComment(groupIDP, eventIDP, apiStrForEventP, apiKeyP ):
  #https://api.meetup.com/2/event_comments?&sign=true&photo-host=public&group_id=18125702&event_id=227594117&page=20  
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")

  UTF8Writer = codecs.getwriter('utf8')
  sys.stdout = UTF8Writer(sys.stdout)  
  per_page = 200
  results_we_got = per_page
  offset = 0
  resCounter =  1
  ## the final dictionary 
  dictToRet={}
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                    "event_id": eventIDP, "group_id": groupIDP,   
                                    "key":apiKeyP, "page":per_page, "offset":offset }, apiStrForEventP)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                if 'meta' in response:
                  results_we_got = response['meta']['count']
                else: 
                  results_we_got =  0   
                if 'results' in response:  
                  for evtItem in response['results']:
                    if 'comment' in evtItem:
                      commentString= evtItem['comment'] 
                    else:
                      commentString ="Unknown"  
                    if 'event_comment_id' in evtItem:
                      eventCommentIDString= evtItem['event_comment_id'] 
                    else:
                      eventCommentIDString= "Unknown"  
                    if 'like_count' in evtItem:
                      likeCountString= evtItem['like_count'] 
                    else:
                      likeCountString = "Unknown"  
                    if 'member_id' in evtItem:
                      memberIDString = evtItem['member_id']
                    else:
                      memberIDString = "Unknown"
                    content = map(unicode, [
                                            eventCommentIDString , commentString, 
                                            likeCountString, memberIDString 
                                           ]
                                 )
                    
                    decoded_content = [x.decode('utf-8').strip() for x in content]                  
                    #print "\t" .join(decoded_content)
                    dictToRet[decoded_content[0]] = [
                                                     decoded_content[1], decoded_content[2], 
                                                     decoded_content[3] 
                                                    ]
                    resCounter += 1   

  time.sleep(1)  
  return dictToRet                                            