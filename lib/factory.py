from artists import Artists
from genres import Genres
from metrics import Metrics
from profiles import Profiles
from services import Services

class ResourceFactory:
  
  def __init__(self, key, secret, ext):
    self.key = key
    self.secret = secret
    self.ext = ext

  def setKey(self, key):
    self.key = key

  def getKey(self):
    return self.key

  def setSecret(self, secret):
    self.secret = secret

  def getSecret(self):
    return self.secret

  def setExt(self, ext):
    self.ext = ext

  def getExt(self):
    return self.ext
  
  def getArtists(self):
    return Artists(self.key, self.secret, self.ext)

  def getGenres(self):
    return Genres(self.key, self.secret, self.ext)

  def getMetrics(self):
    return Metrics(self.key, self.secret, self.ext)

  def getProfiles(self):
    return Profiles(self.key, self.secret, self.ext)

  def getServices(self):
    return Services(self.key, self.secret, self.ext)
