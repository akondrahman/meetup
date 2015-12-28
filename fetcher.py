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
  while (results_we_got == per_page):
                response=execQuery({"sign":"true", "photo-host":"public",  
                                      "zip":zipP, "key":apiKeyP, "page":per_page, "offset":offset }, apiStringP)
                ### response has the results for for the corresponding query 
                time.sleep(1)
                offset += 1
                results_we_got = len(response)
                
                for cnt in xrange(per_page):
                  #print "results inside stuff ... ", response[cnt]
                  #print "debugging stuff: response length{}, current count ={}".format(len(response), cnt)
                  if cnt < len(response):
                    if 'category' in response[cnt]: 
                      group_category_name = response[cnt]['category']['name']
                      group_category_id   = response[cnt]['category']['id']
                      if ((group_category_id==catIDP) and (group_category_name==catNameP)):
                        content = map(unicode, [resCounter, cnt, response[cnt]['id'], response[cnt]['name'], 
                           response[cnt]['members'], response[cnt]['urlname']])
                        #print "inside content: ", content   
                        decoded_content = [x.decode('utf-8').strip() for x in content]                  
                      
                        print "\t" .join(decoded_content)                  
                        resCounter += 1   

  time.sleep(1)      