from resource import Resource

class Artists(Resource):

  def view(self, id):
    return self.get(self.genUrl()+id, "")

  def search(self, id):
    pass

  def ranking(self, id):
    pass

  def add(self, id):
    pass
