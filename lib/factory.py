from artists import Artists
from genres import Genres

class ResourceFactory:
  
  def __init__(self, key, ext, secret):
    self.key = key
    self.ext = ext
    self.secret = secret

  def getArtists(self):
    return Artists(self.key, self.ext, self.secret)

  def getGenres(self):
    return Genres(self.key, self.ext, self.secret)

  def getMetrics(self):
    return Metrics(self.key, self.ext, self.secret)

  def getProfiles(self):
    return Profiles(self.key, self.ext, self.secret)

  def getServices(self):
    return Services(self.key, self.ext, self.secret)
