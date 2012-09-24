from cloudkey import CloudKey, SecLevel

USER_ID = '4ecad6c794a6f67e01001266'
API_KEY = '28836643f2c88a0578254f32ac186b44c13b06af'

cloudkey = CloudKey(USER_ID, API_KEY)
print cloudkey.media.get_embed_url("4f081167f325e119a6000318",
                                   SecLevel.ASNUM | SecLevel.DELEGATE)

# Par exemple pour récupérer l'URL d'un thumbnail (En vrai tu devra gèrer les
# éventuelles erreurs réseau)
print cloudkey.media.info(id="4f081167f325e119a6000318",
                          fields=("assets.jpeg_thumbnail_large.download_url",)
                         )["assets"]["jpeg_thumbnail_large"]["download_url"]

