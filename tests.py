#!/usr/bin/python

from nbs_api import API
import json

def artist_view_test():
  api = API("nbsmobile")
  resp = json.loads(api.artistView("356"))
  if resp["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051":
    print "Artist View Test: Passed"
  else:
    print "Artist View Test: FAILED"

def artist_search_test():
  api = API("nbsmobile");
  resp = json.laods.(api.artistSearch("Kanye"))
  if(resp["music_brainz_id"] == "164f0d73-1234-4e2c-8743-d77bf2191051"):
    print "Artist Search Test: Passed"
  else:
    print "Artist Search Test: FAILED"

def artist_ranking_test():
  pass

def artist_add_test():
  pass

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

print "Tests finished"
