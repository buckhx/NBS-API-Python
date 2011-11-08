from artists import Artists
from genre import Genre

class ResourceFactory:
  
  def __init__(self, key):
    self.key = key

  def getArtists(self):
    return Artists(self.key)

  def getGenre(self):
    return Genre(self.key)
