from resource import Resource

class Profiles(Resource):
  
  def artist(self, id):
    return self.get(self.genUrl( )+"/"+id, "")

  def search(self, url):
    return self.get(self.genUrl( ), {'q':query})
  
  def add(self, profiles):
    data = {}
    data['profiles[]'] = '&&'.join(profiles)
    data['key'] = self.secret
    return self.post(self.genUrl( ), data)
