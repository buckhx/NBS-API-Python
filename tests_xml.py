#!/usr/bin/python

from nbs_api import API
import json

failed = []
passed = 12
total = 12

def artist_view_test():
  global failed
  global passed
  pass

def artist_search_test():
  global failed
  global passed
  pass

def artist_ranking_test():
  global failed
  global passed
  pass

def artist_add_test():
  global failed
  global passed
  pass

def genres_artist_test():
  global failed
  global passed
  pass

def metrics_profile_test():
  global failed
  global passed
  pass
def metrics_artist_test():
  global failed
  global passed
  pass

def profiles_artist_test():
  global failed
  global passed
  pass

def profile_search_test():
  global failed
  global passed
  pass

def profile_search_test():
  global failed
  global passed
  pass

def profile_add_test():
  global failed
  global passed
  pass

def services_list_test():
  global failed
  global passed
  pass

def run( ):
  print ">> Running XML Tests..."
  artist_view_test()
  artist_search_test()
  artist_ranking_test()
  artist_add_test()
  genres_artist_test()
  metrics_profile_test()
  print ">> XML Tests finished"
