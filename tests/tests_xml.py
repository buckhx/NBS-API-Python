#!/usr/bin/python

from nbs_api import API
import xml.dom.minidom

failed = []
passed = 0
total = 11

def artist_view_test():
  global failed
  global passed
  api = API("nbsmobile", ".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.artistView("356"))
  music_id = resp.getElementsByTagName("music_brainz_id")[0].childNodes[0].data
  if(music_id == "164f0d73-1234-4e2c-8743-d77bf2191051"):
    passed += 1
  else:
    failed.append("artist_view_test( )")

def artist_search_test():
  global failed
  global passed
  api = API("nbsmobile", ".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.artistSearch("Kanye"))
  music_id = resp.getElementsByTagName("music_brainz_id")[0].childNodes[0].data
  if(music_id == "164f0d73-1234-4e2c-8743-d77bf2191051"):
    passed += 1
  else:
    failed.append("artist_search_test( )")

def artist_ranking_test():
  global failed
  global passed
  api = API("nbsmobile", ".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  ids = [356, 659, 8309]
  type = "nominal"
  resp = xml.dom.minidom.parseString(api.artistRanking(type, ids))
  elements = resp.getElementsByTagName("name")
  names = []
  for i in elements:
    names.append(i.childNodes[0].data)
  if(names[0] == "Lady Gaga" and names[1] == "Kanye West" and names[2] == "Chiddy Bang"):
    passed += 1
  else:
    failed.append("artist_ranking_test( )")

def artist_add_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  profiles = ["http://www.myspace.com/longmiles"]
  name = "Long Miles"
  resp = xml.dom.minidom.parseString(api.artistAdd(name , profiles))
  message = resp.getElementsByTagName("message")[0].childNodes[0].data
  if(message == "That Artist already exists in our system [#324157]"):
    passed += 1
  else:
    failed.append("artist_ranking_test( )")

def genres_artist_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.genresArtist("356"))
  genre = resp.getElementsByTagName("name")[1].childNodes[0].data
  if(genre == "HipHop"):
    passed += 1
  else:
    failed.append("artist_ranking_test( )")

def metrics_profile_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.metricsProfile("388"))
  plays = resp.getElementsByTagName("value")[0].childNodes[0].data
  if(plays == "308315571"):
    passed += 1
  else:
    failed.append("metrics_profile_test( )")

def metrics_artist_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.metricsArtist("388"))
  service = resp.getElementsByTagName("service")[0].childNodes[0].data
  if(service == "MySpace"):
    passed += 1
  else:
    failed.append("metrics_artist_test( )")

def profiles_artist_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.profilesArtist("356"))
  service = resp.getElementsByTagName("service")[9].childNodes[0].data
  if(service == "MySpace"):
    passed += 1
  else:
    failed.append("profiles_artist_test()")

def profiles_search_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.profilesSearch("http://www.myspace.com/kanyewest"))
  music_id = resp.getElementsByTagName("music_brainz_id")[0].childNodes[0].data
  if(music_id == "164f0d73-1234-4e2c-8743-d77bf2191051"):
    passed += 1
  else:
    failed.append("profile_search_test( )")

def profiles_add_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  profiles = ["http://www.myspace.com/longmiles"]
  resp = xml.dom.minidom.parseString(api.profilesAdd("324157", profiles))
  name = resp.getElementsByTagName("name")[0].childNodes[0].data
  if(name == "Long Miles"):
    passed += 1
  else:
    failed.append("profiles_add_test( )")

def services_list_test():
  global failed
  global passed
  api = API("nbsmobile",".xml", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = xml.dom.minidom.parseString(api.servicesList())
  elements = resp.getElementsByTagName("name")
  names = []
  for i in elements:
    names.append(i.childNodes[0].data)
  if(names[0] == "MYSPACE" and names[12] == "PANDORA"):
    passed += 1
  else:
    failed.append("services_list_test( )")

def run( ):
  print ">> Running XML Tests..."
  artist_view_test()
  artist_search_test()
  artist_ranking_test()
  artist_add_test()
  genres_artist_test()
  metrics_profile_test()
  metrics_artist_test()
  profiles_artist_test()
  profiles_search_test()
  profiles_add_test()
  services_list_test()
  print ">> XML Tests finished"
