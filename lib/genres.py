from resource import Resource

class Genres(Resource):  

	def genreArtist(self, id):
		return self.get(self.genUrl()+id, "")
