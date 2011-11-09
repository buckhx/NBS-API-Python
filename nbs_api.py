from lib.factory import ResourceFactory

class API:

  def __init__(self,key,ext,secret):
    self.factory = ResourceFactory(key,ext,secret)

  def artist(self):
    return self.factory.getArtists( )

  def artistView(self,id):
    return self.artist().view(id)

  def artistSearch(self,name):
    return self.artist( ).search(name)

  def artistRanking(self,type,ids):
    return self.artist().rank(type,ids)

  def artistAdd(self,name, profiles):
    return self.artist().add(name, profiles)

  def genres(self):
    return self.factory.getGenres()

  def genresArtist(self):
    return self.genres.artist( )

