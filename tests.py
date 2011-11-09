#!/usr/bin/python

import tests_json as json
import tests_xml as xml

def run( ):
  print "*********[RUNNING TESTS]*********"
  print ">> JSON tests first because it's cool"
  json.run( )
  print ">> XML tests second because..."
  xml.run( )
  passed = json.passed + xml.passed
  total = json.total + xml.total
  print "*********[FINISHED TESTS]*********"
  print ">> RESULTS:"
  print ">>	"+str(passed)+"/"+str(total)+" passed"
  if (passed < total):
    print ">> FAILURES:"
    failures = json.failed + xml.failed
    for f in failures:
      print ">>     "+f


  print ">>"
  print ">>"
  print ">> Hopefully you didn't break anything..."
  print ">> I know who you are if you did"

run( )
  
