from resource import Resource

# Resources
class Artists(Resource):

  def view(self, id):
    return self.get(self.genUrl()+id, "")
