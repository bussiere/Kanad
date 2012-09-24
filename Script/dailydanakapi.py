import json
import urllib2
import hashlib
import datetime
import time
import random

  
class Api(object):
    def __init__(self,user_id,api_key):
        self.user_id = user_id
        self.api_key = api_key
    
    def normalize(self,input=None):
        output = ''
    
        if type(input) in (list, tuple):
            for element in input:
                if type(element) in (dict, list, tuple):
                    element = self.normalize(element)
                output += str(element)
    
        elif type(input) is dict:
            keys = input.keys()
            keys.sort()
            for key in keys:
                element = input[key]
                if type(element) in (dict, list, tuple):
                    element = self.normalize(element)
                output += '%s%s' % (key, element)
    
        else:
            output = str(input)
    
        return output
    
    def envois(self,request):
        checksum = hashlib.md5(self.user_id + self.normalize(request) + self.api_key).hexdigest()
        auth_token = self.user_id + ':' + checksum
        request["auth"] = auth_token
        request = json.dumps(request)
        
        host = " http://api.dmcloud.net/api"
        req = urllib2.Request(host, request, {'content-type': 'application/json'})
        response_stream = urllib2.urlopen(req)
        response = response_stream.read()
        return response
        
    def request(self,call,args,plus=None):
    
        request = {
            "call": call,
            "args": args
        }
        if plus:
            for key in plus.keys():
                request["args"][key] = plus[key]

        return self.envois(request)
    
    def liste(self,arglist={"fields": [
              "id",
              "created",
              "name"
            ]},page=1,per_page=10):
        
        call = "media.list"
        args =     arglist
        return self.request(call,args)
    
    
    def createTimestamp(self, secondes=86400)
    def creatimestamp(self, annee, mois, jour, heure=0, minute=0):
        n = datetime.datetime(annee, mois, jour, heure, minute)
        return str(time.mktime(n.timetuple())).split(".")[0]
    
    def auth(self,id,timestamp,nonce="12345678",seclevel=0,secdata="",pubsecdata="",urlnoquery=""):
        secu = "%s%s%s%s%s%s%s"%(seclevel,urlnoquery,timestamp,nonce,self.api_key,secdata,pubsecdata)
        print secu
        md5sum = hashlib.md5(secu).hexdigest()
        
        return md5sum
        
    def nonce(self):
        return "%08x" % random.randint(0,16**8-1)

    def get(self, urlnoquery, id, jour=[2012,12,24,0,0], seclevel=0, secdata="",pubsecdata=""):
        timestamp =  self.creatimestamp(jour[0],jour[1],jour[2],jour[3],jour[4])
        nonce = self.nonce()
        md5sum = self.auth(id, timestamp, nonce, seclevel, secdata, pubsecdata, urlnoquery)
        signed_url = "%s?auth=%s-%s-%s-%s" % (urlnoquery,timestamp,seclevel,nonce,md5sum)
        if pubsecdata != "" :
           signed_url  = signed_url +"-%s"%(pubsecdata)

        return signed_url
    
    def getvanilla(self, id, skin="modern1", **kwargs):
        urlnoquery = "http://api.dmcloud.net/player/embed/%s/%s" % (self.user_id, id)
        return self.get(urlnoquery, id, **kwargs) + ("&skin=%s" % skin)
    
    def getStreamurl(self, id, assetname="mp4_h264_aac_ld",assetextension="mp4", **kwargs):
        urlnoquery = "http://cdn.dmcloud.net/route/%s/%s/%s.%s"%(self.user_id,id,assetname,assetextension)
        return self.get(urlnoquery, id, **kwargs)

    def getStreamurl_flv(self, id, **kwargs):
        return self.getStreamurl(id, assetname="flv_h263_mp3", assetextension="flv", **kwargs)


user_id  = '4ecad6c794a6f67e01001266'
api_key  = '28836643f2c88a0578254f32ac186b44c13b06af'
api = Api(user_id,api_key)
print api.liste()
print api.getStreamurl_flv("4ecadbe594a6f67e0300127e")
print api.getStreamurl("4ecadbe594a6f67e0300127e")
print api.getvanilla("4f081167f325e119a6000318")
