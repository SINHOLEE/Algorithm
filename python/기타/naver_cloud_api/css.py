import os
import sys
import urllib.request
client_id = "vo3blf8y6h"
client_secret = "zD8iYL2ANBoR7hER965PdbBONQgq9xK67wwXjR3l"
encText = urllib.parse.quote("반갑습니다 네이버")
data = "speaker=mijin&speed=0&text=" + encText
url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
request.add_header("X-NCP-APIGW-API-KEY", client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)