from cloudkey import CloudKey

USER_ID = '4ecad6c794a6f67e01001266'
API_KEY = '28836643f2c88a0578254f32ac186b44c13b06af'

cloudkey = CloudKey(USER_ID, API_KEY)
medias = cloudkey.media.list()
#url = cloudkey.media.get_embed_url(id=media['id'], seclevel=SecLevel.DELEGATE | SecLevel.ASNUM, expires=time() + 3600)
for m in medias :
	print m


#print url

   def sign_url(self,url, secret, seclevel=None, asnum=None, ip=None, useragent=None, countries=None, referers=None, expires=None):
    # Normalize parameters
        seclevel = seclevel or SecLevel.NONE
        expires = int(expires or time.time() + 7200)
    
        # Compute digest
        (url, unused, query) = url.partition('?')
        secparams = ''
        public_secparams = []
        if not seclevel & SecLevel.DELEGATE:
            if seclevel & SecLevel.ASNUM:
                if not asnum:
                    raise ValueError('ASNUM security level required and no AS number provided.')
                secparams += asnum
            if seclevel & SecLevel.IP:
                if not ip:
                    raise ValueError('IP security level required and no IP address provided.')
                secparams += ip
            if seclevel & SecLevel.USERAGENT:
                if not useragent:
                    raise ValueError('USERAGENT security level required and no user-agent provided.')
                secparams += useragent
            if seclevel & SecLevel.COUNTRY:
                if not countries or len(countries) == 0:
                    raise ValueError('COUNTRY security level required and no coutry list provided.')
                if type(countries) is not list:
                    raise ValueError('Invalid format for COUNTRY, should be a list of country codes.')
                if countries[0] == '-':
                    countries = '-' + ','.join(countries[1:])
                else:
                    countries = ','.join(countries)
                if not re.match(r'^-?(?:[a-zA-Z]{2})(?:,[a-zA-Z]{2})*$', countries):
                    raise ValueError('Invalid format for COUNTRY security level parameter.')
                public_secparams.append('cc=%s' % countries.lower())
            if seclevel & SecLevel.REFERER:
                if not referers or len(referers) == 0:
                    raise ValueError('REFERER security level required and no referer list provided.')
                if type(referers) is not list:
                    raise ValueError('Invalid format for REFERER, should be a list of url strings.')
                public_secparams.append('rf=%s' % urllib.quote_plus(' '.join([referer.replace(' ', '%20') for referer in referers])))
      
    def get_embed_url(self, id, seclevel=None, asnum=None, ip=None, useragent=None, countries=None, referers=None, expires=None, skin=None):
        if type(id) not in (str, unicode):
            raise InvalidParameter('id is not valid')
        url = '%s/embed/%s/%s' % (self._client._base_url, self.user_id, id)
        return self.sign_url(url, self.api_key, seclevel=seclevel, asnum=asnum, ip=ip, useragent=useragent, countries=countries, referers=referers, expires=expires) \
            + ('skin=%s' % skin if skin else '')
        
    def get_qtref_url(self, id, seclevel=None, asnum=None, ip=None, useragent=None, countries=None, referers=None, expires=None):
        if type(id) not in (str, unicode):
            raise InvalidParameter('id is not valid')
        url = '%s/stream/%s/%s.mov' % (self._client._base_url, self.user_id, id)
        return self.sign_url(url, self.api_key, seclevel=seclevel, asnum=asnum, ip=ip, useragent=useragent, countries=countries, referers=referers, expires=expires)
        
    def get_stream_url(self, id, asset_name='mp4_h264_aac', seclevel=None, asnum=None, ip=None, useragent=None, countries=None, referers=None, expires=None, download=False, filename=None, version=None, protocol=None, cdn_url='http://cdn.dmcloud.net'):
        if type(id) not in (str, unicode):
            raise InvalidParameter('id is not valid')
        if protocol not in (None, 'hls', 'rtmp', 'hps', 'http'):
            raise InvalidParameter('%s is not a valid streaming protocol' % protocol)
        version = '-%d' % version if version else ''
        if asset_name.startswith('jpeg_thumbnail_'):
            base_url = cdn_url.replace('cdn.', 'static.')
            ts = '-%d' % int(expires) if expires else ''
            return '%s/%s/%s/%s%s%s.jpeg' % (base_url, self.user_id, id, asset_name, ts, version)
        extension = asset_name.split('_')[0]
        if extension == 'f4f':
            extension = 'f4m'
        if download or filename:
            protocol = 'http'
        url = '%s/route%s/%s/%s/%s%s.%s' % (cdn_url, '/%s' % protocol if protocol else '', self.user_id, id, asset_name, version, extension)
        if filename:
            url = '%s%s%s' % (url, '&' if '?' in url else '?', urllib.urlencode({'filename': filename.encode('utf-8', 'ignore')}))
        return self.sign_url(url, self.api_key, seclevel=seclevel, asnum=asnum, ip=ip, useragent=useragent, countries=countries, referers=referers, expires=expires)
    