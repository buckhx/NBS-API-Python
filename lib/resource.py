import urllib as rest
import inspect

class Resource:
  base = ".api3.nextbigsound.com/"

  # Constructor:
  #  Default value for ext is json
  #  If xml is wanted it must be explicitly passed
  def __init__(self, key, ext=".json"):
    self.key = key
    self.ext = ext

  # Resource has an association with
  # both Artists and Genre.
  # Genre and Artists inherit from Resource...

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
    resource = self.__class__.__name__
    method = inspect.stack()[1][3]
    return ("http://" + self.key + Resource.base + resource + "/" + method + "/").lower()

