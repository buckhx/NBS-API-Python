from resource import Resource

class Metrics(Resource):

  def profile(self, id, opt=[]):
    if opt == []:
      # print repr(self.get(self.genUrl( )+"/"+id, ""))
      return self.get(self.genUrl( )+"/"+id, "")
    else:
      data = {}
      data['start'] = opt[0]
      data['end'] = opt[1]
      data['metric'] = opt[2]
      return self.post(self.genUrl( )+"/"+id, data)

  def artist(self, id, opt=[]):
    if opt == []:
      return self.get(self.genUrl( )+"/"+id, "")
    else:
      data = {}
      data['start'] = opt[0]
      data['end'] = opt[1]
      data['metric'] = opt[2]
      return self.post(self.genUrl( )+"/"+id, data)
