#!/usr/bin/python

from nbs_api import API
import json

failed = [""]
passed = 0
total = 11

def artist_view_test():
  global failed
  global passed
  api = API("nbsmobile")
  resp = json.loads(api.artistView("356"))
  if resp["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051":
    passed += 1
  else:
    failed += ["artist_view_test_( )"]

def artist_search_test():
  global failed
  global passed
  api = API("nbsmobile");
  resp = json.loads(api.artistSearch("Kanye"))
  if resp["356"]["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051":
    passed += 1
  else:
    failed += ["artist_search_test( )"]

def artist_ranking_test():
  global failed
  global passed
  api = API("nbsmobile")
  ids = [356, 659, 8309]
  type = "nominal"
  resp = json.loads(api.artistRanking(type, ids))
  if (resp[0]["name"] == "Lady Gaga"):
    passed += 1
  else:
    failed += ["artist_ranking_test( )"]

def artist_add_test():
  global failed
  global passed
  api = API("nbsmobile", "ad644d582c7dcf7dc29479ff2d4df1ef")
  name = "Long Miles"
  profiles = ["http://www.facebook.com/longmiles"]
  resp = json.loads(api.artistAdd(name, profiles))
  if resp['message'] == "That Artist already exists in our system [#324157]":
    passed += 1
  else:
    failed += ["artist_add_test( )"]

def genres_artist_test():
  global failed
  global passed
  api = API("nbsmobile")
  resp = json.loads(api.genresArtist("356"))
  if resp["2"]["name"] == "HipHop":
    passed += 1
  else:
    failed += ["genres_artist_test( )"]

def metrics_profile_test():
  global failed
  global passed
  api = API("nbsmobile")
  resp = json.loads(api.metricsProfile("388"))
  if resp["plays"] and resp["fans"] and resp["views"]:
    passed += 1
  else:
    failed += ["metrics_profile_test( )"]

def metrics_artist_test():
  global failed
  global passed
  api = API("nbsmobile")
  resp = json.loads(api.metricsArtist("356"))
  if resp[0]["Service"]["name"] == "MySpace":
    passed += 1
  else:
    failed += ["metrics_artist_test( )"]

def profiles_artist_test():
  global failed
  global passed
  api = API("nbsmobile")
  resp = json.loads(api.profilesArtist("356"))
  if resp["388"]["name"] == "MySpace":
    passed += 1
  else:
    failed += ["profiles_artist_test( )"]

def profiles_search_test():
  global failed
  global passed
  api = API("nbsmobile");
  resp = json.loads(api.profilesSearch("http://www.myspace.com/kanyewest"))
  if resp["356"]["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051":
    passed += 1
  else:
    failed += ["profiles_search_test( )"]

def profiles_add_test():
  global failed
  global passed
  api = API("nbsmobile", "ad644d582c7dcf7dc29479ff2d4df1ef")
  name = "Long Miles"
  profiles = ["http://www.myspace.com/longmiles"]
  resp = json.loads(api.profilesAdd("324157", profiles))
  if resp['name'] == "Long Miles":
    passed += 1
  else:
    failed += ["artist_add_test( )"]

def services_list_test():
  global failed
  global passed
  api = API("nbsmobile")
  resp = json.loads(api.servicesList())
  if resp["1"]["name"] == "MYSPACE" and resp["36"]["name"] == "PANDORA":
    passed += 1
  else:
    failed += ["artist_add_test( )"]

def run( ):
  print ">> Running JSON Tests..."
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
  print ">> JSON Tests finished"
