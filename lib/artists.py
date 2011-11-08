from resource import Resource

class Artists(Resource):

  def view(self, id):
    return self.get(self.genUrl()+id, "")
