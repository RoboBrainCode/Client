from s3Upload import Upload
colorred = "\033[01;31m{0}\033[00m"
colorgrn = "\033[1;36m{0}\033[00m"

class RoboBrainAPI:
   
    def __init__(self,username,password,apikey,apisecret,contname):
        self.feeds = []
        self.username=username
        self.password=password
        self.apikey=apikey
        self.apisecret=apisecret
        self.s3 = Upload(apikey,apisecret)
        self.contname = contname

    def addFeed(self,feed):
        self.feeds.append(feed)

    def fixMedia(self):
        import os
        import re
        for f in self.feeds:
            for idx,m in enumerate(f['media']):
                fN = os.path.basename(m)
                ext = os.path.splitext(m)[1][1:]
                tPath = '/'
		noDol = re.sub('\$','',f['text']);
                hashS = re.sub('\.','',noDol).split('#')
                for z in range(1,len(hashS)):
                    tPath = tPath+hashS[z].split(' ')[0]+'/'
                pathN = self.contname+'/'+ext+tPath+fN
                print colorgrn.format("s3 Upload attempt")
                print "\t",m
                self.s3.upload(m,pathN)
                f['media'][idx]=pathN

    def postJSON(self,feed,url):
        import requests
        import json
        headers = {'content-type': 'application/json'}

	resp = requests.post(url, data=json.dumps(feed), headers=headers,auth=(self.username, self.password))
        print colorgrn.format("Attempt to HTTP Post Request to the Brain")
        print "\t Response:",resp
        print "\t",resp.text

    def push2Brain(self,url):
        self.fixMedia()
        for f in self.feeds:
            f['username']=self.contname
            f['hashtags']=''
            for wordd in f['text'].split():
                if wordd[0]=='#':
                    f['hashtags']=f['hashtags']+' '+wordd[1:].lower()
            self.postJSON(f,url)        
        del self.feeds[:]
