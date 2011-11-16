from resource import Resource

class Artists(Resource):

  def view(self, id):
    return self.get(self.genUrl( )+"/"+id, "")

  def search(self, query):
    return self.get(self.genUrl( ), {'q':query})

  def rank(self, type, ids):
    uids = ""    
    for i in ids:
	uids += str(i) + '-'
    uids = uids[:-1]
    return self.get(self.genUrl( ) + "/" + type + "/" + uids, "")

  def add(self, name, profiles):
    if (self.secret == ""):
      raise Exception("A private key is needed")
    else:
      data = {}
      data['name'] = name
      data['profiles[]'] = '&&'.join(profiles)
      data['key'] = self.secret
      return self.post(self.genUrl( ), data)

