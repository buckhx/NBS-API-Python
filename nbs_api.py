from lib.factory import ResourceFactory

class API:

  def __init__(self,key):
    self.factory = ResourceFactory(key)

  def artist(self):
    return self.factory.getArtists()

  def artistView(self,id):
    return self.artist().view(id)

  def artistSearch(self,name):
    return self.artist().search(name)

  def artistRanking(self,type,ids):
    return self.artist().ranking(type,ids)

  def artistAdd(self,name,profiles):
    return self.artist().add(name,profiles)

  def genre(self):
    return self.factory.getGenre()

  def genreArtist(self):
    return self.genre.artist()

