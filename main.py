import pywikibot
from pywikibot import pagegenerators
import tweepy
		
# My baby bot
class NukeBot(object):
	def __init__(self):
		self.refInfo = self.makeList()
		while True:
			self.listen()
	
	def listen(self):
		checkList = self.makeList()
		for check in checkList:
			for page in self.refInfo:
				if page.Title == check.Title:
					found = True
					if page.Revision.sha1 != check.Revision.sha1:
						self.update(check)
			if found != True:
				self.refInfo.append(check)
			else:
				found = False
			
	def makeList(self):
		self.site = pywikibot.Site()
		self.cat = pywikibot.Category(self.site,'Category:Nuclear power')
		self.gen = pagegenerators.CategorizedPageGenerator(self.cat)
		self.refInfo = []
		self.err = False
		for page in self.gen:
			list.append(page)
		return list
		
	def update(self,file):
		updateList = []
		for page in self.refInfo:
			if page.Title == file.Title:
				updateList.append(file)
				tweet(file)
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
	api.update_status(status)

# Make the twitter status to tweet
def makeStatus(edit):
	title = edit.Title
	url = edit.Url
	
	

def main():
	
	bot = NukeBot()
		
		
if __name__ == "__main__":
    try:
        main()
    finally:
        pywikibot.stopme()
