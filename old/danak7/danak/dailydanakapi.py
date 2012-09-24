import json
import urllib2
import hashlib
import datetime
import time

  
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
        if plus :
            for key in plus.keys() :
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
    
    
    def creatimestamp(self,annee,mois,jour,heure=0,minute=0):
        print annee, mois,jour,heure,minute
        n=datetime.datetime(annee, mois,jour,heure,minute)
        return str(time.mktime(n.timetuple())).split(".")[0]
    
    def auth(self,id,timestamp,nonce="12345678",seclevel=0,secdata="",pubsecdata="",urlnoquery=""):
        secu = "%s%s%s%s%s%s%s"%(seclevel,urlnoquery,timestamp,nonce,self.api_key,secdata,pubsecdata)
        print secu
        md5sum = hashlib.md5(secu).hexdigest()
        
        return md5sum
    
    def getStreamurl_flv(self,id,jour=[2012,12,24,0,0],nonce="12345678",seclevel=0,secdata="",pubsecdata=""):
        return  self.getStreamurl(id,jour,nonce,seclevel,secdata,pubsecdata,assetname="flv_h263_mp3",assetextension="flv")
        
        
    def getStreamurl(self,id,jour=[2012,12,24,0,0],nonce="12345678",seclevel=0,secdata="",pubsecdata="",assetname="mp4_h264_aac_ld",assetextension="mp4"):
            timestamp =  self.creatimestamp(jour[0],jour[1],jour[2],jour[3],jour[4])
            print timestamp
            urlnoquery = "http://cdn.dmcloud.net/route/%s/%s/%s.%s"%(self.user_id,id,assetname,assetextension)
            md5sum = self.auth(id,timestamp,nonce,seclevel,secdata,pubsecdata,urlnoquery)
            signed_url = "%s?auth=%s-%s-%s-%s"%(urlnoquery,timestamp,seclevel,nonce,md5sum)
            if pubsecdata != "" :
               signed_url  = signed_url +"-%s"%(pubsecdata)
            return signed_url
    
    def getvanilla(self,id,jour=[2012,12,24,0,0],nonce="12345678",seclevel=0,secdata="",pubsecdata="",skin="modern1"):
            timestamp =  self.creatimestamp(jour[0],jour[1],jour[2],jour[3],jour[4])
            print timestamp
            urlnoquery = "http://api.dmcloud.net/embed/%s/%s"%(self.user_id,id)
            md5sum = self.auth(id,timestamp,nonce,seclevel,secdata,pubsecdata,urlnoquery)
            signed_url = "%s?auth=%s-%s-%s-%s&skin=%s"%(urlnoquery,timestamp,seclevel,nonce,md5sum,skin)
            if pubsecdata != "" :
               signed_url  = signed_url +"-%s"%(pubsecdata)
            return signed_url
    

user_id  = '4ecad6c794a6f67e01001266'
api_key  = '28836643f2c88a0578254f32ac186b44c13b06af'
api = Api(user_id,api_key)
print api.liste()
print api.getStreamurl_flv("4ecadbe594a6f67e0300127e")
print api.getStreamurl("4ecadbe594a6f67e0300127e")
print api.getvanilla("4ecadbe594a6f67e0300127e")