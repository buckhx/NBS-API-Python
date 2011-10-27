from lib.resource import Resource

class API:

  def __init__(self,key):
    self.resource = Resource(key)

  def artist(self):
    return self.resource.getArtists()

  def artistView(self,id):
    return self.artist().view(id)

  def artistSearch(self,name):
    return self.artist().search(name)

  def artistRanking(self,type,ids):
    return self.artist().ranking(type,ids)

  def artistAdd(self,name,profiles):
    return self.artist().add(name,profiles)

  def genre(self):
    return self.getGenre()

  def genreArtist(self):
    return self.genre.artist()

