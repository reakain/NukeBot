import pywikibot
from pywikibot import pagegenerators
import itertools
import tweepy
		
# My baby bot
class NukeBot(object):
	def __init__(self):
		self.refInfo = self.makeList()
		count = 0
		while True:
			self.listen()
			count = count+1
			print(count)
	
	def listen(self):
		checkList = self.makeList()
		for check in checkList:
			for page in self.refInfo:
				if page.title == check.title:
					found = True
					#print(itertools.islice(page.revisions(),1)._sha1)
					#print(next(page.revisions()).revid)
					#print(next(check.revisions()).revid)
					if next(page.revisions()).revid != next(check.revisions()).revid:
						self.update(check)
			if found != True:
				self.refInfo.append(check)
			else:
				found = False
			
	def makeList(self):
		self.site = pywikibot.Site()
		self.cat = pywikibot.Category(self.site,'Category:Nuclear power')
		self.gen = pagegenerators.CategorizedPageGenerator(self.cat)
		self.err = False
		someList = []
		for page in self.gen:
			someList.append(page)
		self.cat = pywikibot.Category(self.site,'Category:Nuclear technology')
		self.gen = pagegenerators.CategorizedPageGenerator(self.cat)
		for page in self.gen:
			someList.append(page)
		return someList
		
	def update(self,file):
		updateList = []
		for page in self.refInfo:
			if page.title == file.title:
				updateList.append(file)
				print(file.title)
				#tweet(file)
			else:
				updateList.append(page)
		self.refInfo = []
		self.refInfo = updateList

# Tweet your shit
def tweet(edit):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	status = makeStatus(edit)
	try:
		api.update_status(status)
	except api.TweepError as e:
		print(e.reason)

# Make the twitter status to tweet
def makeStatus(edit):
	title = edit.title
	url = edit.url
	
	

def main():
	
	bot = NukeBot()

if __name__ == "__main__":
	try:
		main()
	finally:
		pywikibot.stopme()