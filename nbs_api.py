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

  def genresArtist(self,id):
    return self.genres().artist(id)

  def metrics(self):
    return self.factory.getMetrics()

  def metricsProfile(self, id, opt=[]):
    return self.metrics().profile(id, opt)

