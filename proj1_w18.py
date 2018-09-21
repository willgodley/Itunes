import requests
import json
import webbrowser as wb

class Media:

	def __init__(self, title = "No Title", author = "No Author", releaseYear = "0", json = None):

		if not isinstance(json, dict):
			self.title = title
			self.author = author
			self.releaseYear = releaseYear
		else:
			self.author = json['artistName']
			self.releaseYear = json['releaseDate'][:4]
			if json["wrapperType"] == "track":
				self.title = json["trackName"]
			else:
				self.title = json["collectionName"]
			self.rawData = json

	def __str__(self):
		return "{} by {} ({})".format(self.title, self.author, self.releaseYear)

	def __len__(self):
		return "0"

## Other classes, functions, etc. should go here

class Song(Media):

	def __init__(self, title = "No Title", author = "No Author", releaseYear = "2000",
	 	albumTitle = "No Album Title", genre = "No Genre", trackLength = "0", json = None):

		if not isinstance(json, dict):
			super().__init__(title, author, releaseYear)
			self.album = albumTitle
			self.genre = genre
			self.length = str(trackLength)
		else:
			super().__init__(json = json)
			self.album = json["collectionName"]
			self.genre = json["primaryGenreName"]

			unrounded = str(json["trackTimeMillis"] / 1000).split(".")
			rounded = unrounded[0]
			if int(unrounded[1][0]) > 4:
				rounded = int(unrounded[0])
				rounded += 1
			self.length = str(rounded)

	def __str__(self):
		return super().__str__() + " [" + self.genre + "]"

	def __len__(self):
		return self.length

class Movie(Media):

	def __init__(self, title="No Title", author="No Author", releaseYear="2000",
		rating = "G", movieLength = "100", json = None):

		if not isinstance(json, dict):
			super().__init__(title, author, releaseYear)
			self.rating = rating
			self.length = movieLength
		else:
			super().__init__(json = json)
			self.rating = json["contentAdvisoryRating"]

			unrounded = str(json["trackTimeMillis"] / (1000 * 60)).split(".")
			rounded = unrounded[0]
			if int(unrounded[1][0]) > 4:
				rounded = int(unrounded[0])
				rounded += 1
			self.length = str(rounded)


	def __str__(self):
		return super().__str__() + " [" + self.rating + "]"

	def __len__(self):
		return self.length

def apiCall(search):

	objects = []

	try:
		itunesResponse = requests.get('https://itunes.apple.com/search?', params = {
			'term' : search,
			'country': 'US'
			})
		data = json.loads(itunesResponse.text)
		itunesResults = data['results']

	except:
		print("Error. Make sure you are connected to the internet.")

	for item in itunesResults:
		try:
			if item['kind'] == 'song':
				objects.append(Song(json = item))
		except:
			pass
	for item in itunesResults:
		try:
			if item['kind'] == 'feature-movie':
				objects.append(Movie(json = item))
		except:
			pass
	for item in itunesResults:
		try:
			if item['kind'] != 'song' and item['kind'] != 'feature-movie':
				objects.append(Media(json = item))
		except:
			objects.append(Media(json = item))
	return objects


if __name__ == "__main__":

	print()
	print("Enter a search term, or “exit” to quit: ")
	search = input("> ")
	print()

	while search != "exit":

		items = apiCall(search)

		if len(items) == 0:
			print("No search results.")
			print()
			print("Enter a search term, or “exit” to quit: ")
			search = input("> ")
			continue

		counter = 1
		moviePrinted = False
		mediaPrinted = False
		songPrinted = False

		for item in items:

			if not songPrinted:
				try:
					junk = item.genre
					print()
					print('SONGS')
					songPrinted = True
				except:
					pass

			if not moviePrinted:
				try:
					junk = item.rating
					print()
					print('MOVIES')
					moviePrinted = True
				except:
					pass

			if item.__len__() == '0' and mediaPrinted == False:
				print()
				print('OTHER MEDIA')
				mediaPrinted = True

			print(str(counter) + " " + item.__str__())
			counter += 1

		print()

		if not songPrinted:
			print("No Song Results.")
			print()
		if not moviePrinted:
			print("No Movie Results.")
			print()
		if not mediaPrinted:
			print("No Other Media Results.")
			print()

		print("Enter a number for more info, or another search term, or exit: ")
		search = input("> ")
		print()

		while True:
			try:
				choice = int(search)
				i = choice - 1
				url = items[i].rawData['trackViewUrl']
				print('Launching ' + url + ' in web browser...')
				print()
				wb.open_new(url)

				print("Enter search query, the item number for more info, or exit: ")
				search = input("> ")
				print()
			except:
				break

	print("Bye!")
	print()
