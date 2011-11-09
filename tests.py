#!/usr/bin/python

from nbs_api import API
import json

def artist_view_test():
  api = API("nbsmobile",".json", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  resp = json.loads(api.artistView("356"))
  if resp["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051":
    print "Artist View Test: Passed"
  else:
    print "Artist View Test: FAILED"

def artist_search_test():
  api = API("nbsmobile",".json", 'ad644d582c7dcf7dc29479ff2d4df1ef');
  resp = json.loads(api.artistSearch("Kanye"))
  if resp["356"]["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051":
    print "Artist Search Test: Passed"
  else:
    print "Artist Search Test: FAILED"

def artist_ranking_test():
  api = API("nbsmobile", ".json", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  ids = [356, 659, 8309]
  type = "nominal"
  resp = json.loads(api.artistRanking(type, ids))
  if (resp[0]["name"] == "Lady Gaga"):
    print "Artist Rank Test: Passed"
  else:
    print "Artist Rank Test: FAILED"

def artist_add_test():
  api = API("nbsmobile",".json", 'ad644d582c7dcf7dc29479ff2d4df1ef')
  name = "Long Miles"
  profiles = ["http://www.facebook.com/longmiles"]
  resp = json.loads(api.artistAdd(name, profiles))
  if resp['message'] == "That Artist already exists in our system [#324157]":
    print "Artist Add Test: Passed"
  else:
    print "Artist Add Test: FAILED"

def genres_artist_test():
  pass

def metrics_profile_test():
  pass

def metrics_artist_test():
  pass

def profiles_artist_test():
  pass

def profile_search_test():
  pass

def profile_search_test():
  pass

def profile_add_test():
  pass

def services_list_test():
  pass

print "Running Tests..."

artist_view_test()
artist_search_test()
artist_ranking_test()
artist_add_test()

print "Tests finished"
