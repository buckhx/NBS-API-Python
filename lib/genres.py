from resource import Resource

class Genres(Resource):

  def artist(self, id):
    return self.get(self.genUrl( )+"/"+id, "")

