#Python Wrapper for the Next Big Sound API
10/27/2011

##Contributors:

- Buck Heroux
- Sean Smith
- James B. Fitzgerald
- Omar Sulehria
- Charles McClung
- Michael Odbert

##Conventions
- Use 2 spaces for indentation

Documentation should go here [markdown]
An article for each public method

## artists.py

###def view(self, id):
###\t  return self.get(self.genUrl( )+"/"+id, "")

> *id* is the artists id ex: Kanye West = 356

###def search(self, query):
###  return self.get(self.genUrl( ), {'q':query})

> *query* is the artist's name

###def rank(self, type, ids):
###   ids = ""
###   for i in ids:
###     uids += str(i) + '-'
###  uids = uids\[:-1]\
###   return self.get(self.genUrl( ) + "/" + type + "/" + uids, "")

> *type* is either nominal/velocity/acceleration
> *ids* is a list of artist id ex: \[356, 357, 358\]

###def add(self, name, profiles):
###  data = {}
###  data\['name'\] = name
###  data\['profiles\[\]'\] = '&&'.join(profiles)
###  data\['key'\] = self.secret
###  return self.post(self.genUrl( ), data)

> *name* is the name of the artist you want to add
> *profiles* is a list of profile urls ex: \["http://www.facebook.com/kanyewest", "http://www.myspace.com/kanyewest"\]

## genres.py

###def artist(self, id):
###    return self.get(self.genUrl( )+"/"+id, "")

> *id* is the artist id

## metrics.py

###def profile(self, id, opt=[]):
###  if opt == []:
###    return self.get(self.genUrl( )+"/"+id, "")
###  else:
###    data = {}
###    data\['start'\] = opt\[0\]
###    data\['end'\] = opt\[1\]
###    data\['metric'\] = opt\[2\]
###    return self.post(self.genUrl( )+"/"+id, data)*

> Tricky thing here is that there's optional post parameters.
> ie: opt is defaulted to an empty list
> 
> If there are not optional post parameters for metrics than
> just get the metrics of a profile with id *id*
> 
> If there are option parameters then we need to post them.
> You need to checkout the documentation on python urrlib for
> how the mapping works from variable name to value

###def artist(self, id, opt=\[\]):
###  if opt == \[\]:
###    return self.get(self.genUrl( )+"/"+id, "")
###  else:
###    data = {}
###    data\['start'\] = opt\[0\]
###    data\['end'\] = opt\[1\]
###    data\['metric'\] = opt\[2\]
###    return self.post(self.genUrl( )+"/"+id, data)

> Tricky thing here is that there's optional post parameters.
> ie: opt is defaulted to an empty list
> 
> If there are not optional post parameters for metrics than
> just get the metrics of a profile with id *id*
> 
> If there are option parameters then we need to post them.
> You need to checkout the documentation on python urrlib for
> how the mapping works from variable name to value

## profiles.py

###def artist(self, id):
###  return self.get(self.genUrl( )+"/"+id, "")

> *id* is the artist id

###def search(self, url):
###  return self.get(self.genUrl( ), {'u':url})
> *url* is the profiles url ex: http://www.myspace.com

###def add(self, id, profiles):
###  data = {}
###  data\['profiles\[\]'\] = '&&'.join(profiles)
###  data\['key'\] = self.secret
###  return self.post(self.genUrl( )+"/"+id, data)

> *id* is the artist id
>
> *profiles* is a list of profile urls to add to this artist's profile

## services.py

###def list(self):
###  return self.get(self.genUrl( )\[:-5\], "")

> Retrieve all the social media sites that we support
