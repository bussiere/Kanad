from django.db import models

# Create your models here.
class ClefUser(models.Model):
        Clef= models.CharField(max_length=300,null=True,blank=True)
        Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
        def ___str__(self):
             return self.Clef
        def __unicode__(self):
             return self.Clef
         
         
class ClefApi(models.Model):
        Clef= models.CharField(max_length=300,null=True,blank=True)
        Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
        def ___str__(self):
             return self.Clef
        def __unicode__(self):
             return self.Clef
         
       
class CoupleClef(models.Model):
        Nom = models.CharField(max_length=300,null=True,blank=True)
        ClefUser= models.ForeignKey(ClefUser,null=True,blank=True)
        ClefApi= models.ForeignKey(ClefApi,null=True,blank=True)
        def ___str__(self):
             return self.Nom
        def __unicode__(self):
             return self.Nom
         
         
#foutre les urls dans une classe les urls d'api     
class Api(models.Model):
        Nom = models.CharField(max_length=300,null=True,blank=True)
        CoupleClef= models.ForeignKey(CoupleClef,null=True,blank=True)

        
        
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
        
        
            checksum = hashlib.md5(self.CoupleClef.ClefUser.Clef + self.normalize(request) + self.CoupleClef.ClefApi.Clef).hexdigest()
            
            auth_token = self.CoupleClef.ClefUser.Clef + ':' + checksum
            
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
            secu = "%s%s%s%s%s%s%s"%(seclevel,urlnoquery,timestamp,nonce,self.CoupleClef.ClefApi.Clef,secdata,pubsecdata)
            md5sum = hashlib.md5(secu).hexdigest()
            
            return md5sum
        
        def getStreamurl_flv(self,id,jour=[2012,12,24,0,0],nonce="12345678",seclevel=0,secdata="",pubsecdata=""):
            return  self.getStreamurl(id,jour,nonce,seclevel,secdata,pubsecdata,assetname="flv_h263_mp3",assetextension="flv")
            
            
        def getStreamurl(self,id,jour=[2012,12,24,0,0],nonce="12345678",seclevel=0,secdata="",pubsecdata="",assetname="mp4_h264_aac_ld",assetextension="mp4"):
                timestamp =  self.creatimestamp(jour[0],jour[1],jour[2],jour[3],jour[4])
                print timestamp
                urlnoquery = "http://cdn.dmcloud.net/route/%s/%s/%s.%s"%(self.CoupleClef.ClefUser.Clef,id,assetname,assetextension)
                md5sum = self.auth(id,timestamp,nonce,seclevel,secdata,pubsecdata,urlnoquery)
                signed_url = "%s?auth=%s-%s-%s-%s"%(urlnoquery,timestamp,seclevel,nonce,md5sum)
                if pubsecdata != "" :
                   signed_url  = signed_url +"-%s"%(pubsecdata)
                return signed_url
        
        def getvanilla(self,id,jour=[2012,12,24,0,0],nonce="12345678",seclevel=0,secdata="",pubsecdata="",skin="modern1"):
                timestamp =  self.creatimestamp(jour[0],jour[1],jour[2],jour[3],jour[4])
                print timestamp
                urlnoquery = "http://api.dmcloud.net/embed/%s/%s"%(self.CoupleClef.ClefUser.Clef,id)
                md5sum = self.auth(id,timestamp,nonce,seclevel,secdata,pubsecdata,urlnoquery)
                signed_url = "%s?auth=%s-%s-%s-%s&skin=%s"%(urlnoquery,timestamp,seclevel,nonce,md5sum,skin)
                if pubsecdata != "" :
                   signed_url  = signed_url +"-%s"%(pubsecdata)
                return signed_url
        
        def ___str__(self):
             return self.Nom
        def __unicode__(self):
             return self.Nom
    