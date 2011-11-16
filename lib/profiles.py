from resource import Resource

class Profiles(Resource):
  
  def artist(self, id):
    return self.get(self.genUrl( )+"/"+id, "")

  def search(self, url):
    return self.get(self.genUrl( ), {'u':url})
  
  def add(self, id, profiles):
    if (self.secret == ""):
      raise Exception("A private key is needed")
    else:
      data = {}
      data['profiles[]'] = '&&'.join(profiles)
      data['key'] = self.secret
      return self.post(self.genUrl( )+"/"+id, data)
