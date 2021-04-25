from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import requests
import base64
import datetime
import hashlib
import hmac
import binascii
import codecs
import pytz

# Create your views here.

def getAccessToken():
    client_id = 'b95e5def-0f10-453b-acf2-ff71b4e0e6f4'
    client_secert = 'abd3447f-0f2a-4082-838b-4d735301c44a'

    base = client_id+':'+client_secert

    encode = base64.b64encode(base.encode("utf-8")) 

    r = requests.post('https://sandbox.bca.co.id:443/api/oauth/token', headers={"Authorization":"Basic "+encode.decode("utf-8"), "Content-Type":"application/x-www-form-urlencoded"}, data={"grant_type":"client_credentials"})

    response = json.loads(r.content)

    return response

def generateSignature(HTTPMethod, RelativeUrl, AccessToken, requestBody, timestamp):

    api_secret = b"8d372247-bdca-4f85-aa96-dfa927518a39"

    lower = hashlib.sha256(bytearray.fromhex(requestBody)).hexdigest().lower()

    stringToSign = HTTPMethod+":"+RelativeUrl+":"+AccessToken+":"+lower+":"+timestamp

    signature = hmac.new(api_secret, stringToSign.encode('utf-8'), hashlib.sha256).hexdigest()
    
    return signature

def balance(request):

    tz = pytz.timezone('Asia/Jakarta')
    datetime_now = datetime.datetime.now(tz=tz).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    timestamp = datetime_now+"+07.00"

    api_key = "ef18ff24-a5e3-4c2d-9c3a-32853ec464da"
    HTTPMethod = 'GET'
    RelativeUrl = '/banking/v3/corporates/BCAAPI2016/accounts/0201245680'
    AccessToken = getAccessToken()['access_token']
    requestBody = ""

    header = {
        "X-BCA-Signature" : generateSignature(HTTPMethod, RelativeUrl, AccessToken, requestBody, timestamp),
        "Authorization" : "Bearer"+" "+AccessToken,
        "X-BCA-Key" : api_key,
        "X-BCA-Timestamp" : timestamp,
    }
    
    balanceRequest = requests.get('https://sandbox.bca.co.id:443/banking/v3/corporates/BCAAPI2016/accounts/0201245680', headers=header)

    response = json.loads(balanceRequest.content)
    print(response)
    
    return HttpResponse(json.dumps(response), content_type="application/json")

def statement(request):

    tz = pytz.timezone('Asia/Jakarta')
    datetime_now = datetime.datetime.now(tz=tz).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    timestamp = datetime_now+"+07.00"

    api_key = "ef18ff24-a5e3-4c2d-9c3a-32853ec464da"
    HTTPMethod = 'GET'
    RelativeUrl = '/banking/v3/corporates/BCAAPI2016/accounts/0201245680/statements?EndDate=2016-09-01&StartDate=2016-09-01'
    AccessToken = getAccessToken()['access_token']
    requestBody = ""

    header = {
        "X-BCA-Signature" : generateSignature(HTTPMethod, RelativeUrl, AccessToken, requestBody, timestamp),
        "Authorization" : "Bearer"+" "+AccessToken,
        "X-BCA-Key" : api_key,
        "X-BCA-Timestamp" : timestamp,
    }
    print(header)
    
    statementRequest = requests.get('https://sandbox.bca.co.id:443/banking/v3/corporates/BCAAPI2016/accounts/0201245680/statements?EndDate=2016-09-01&StartDate=2016-09-01', headers=header)

    response = json.loads(statementRequest.content)
    print(response)
    
    return HttpResponse(json.dumps(response), content_type="application/json")

def getMovie(request):
    query = """ 
    {
    movies{
        id
        title
        actors{
            name
            movieName
        }
        year
    }
    }
    """
    data = {"query": query}
    json_data = json.dumps(data)
    response = requests.post('http://127.0.0.1:8000/graphql/', json=data)

    responses = json.loads(response.content)

    return HttpResponse(json.dumps(responses), content_type="application/json")

