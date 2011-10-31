import urllib as rest
import inspect

class Resource(object):
  base = ".api3.nextbigsound.com/"

  def __init__(self,key):
    self.key = key
    self.ext = ".json"


  def setXML(self):
    self.ext = ".xml"

  def getArtists(self):
    return Artists(self.key)

  def getGenre(self):
    return Genre(self.key)

  #add more resources...

  def get(self,url,params):
    url = url + self.ext + rest.urlencode(params)
    return rest.urlopen(url).read()

  def post(self,url,data):
    url = url + self.ext
    data = rest.urlencode(data)
    return rest.urlopen(url,data).read()

  # generates url based on method called and resource used
  #   takes the resource and method name EXACTLY as defined
  def genUrl(self):
    resource = type(self).__name__
    method = inspect.stack()[1][3] 
    return ("http://" + self.key + Resource.base + resource + "/" + method + "/").lower()
