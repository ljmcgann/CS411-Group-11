from flask import Flask
import requests

client = {
	'client_id'      : '6f30ec7e477d4fe0aa3c1eb5d99dc519', 
	'client_secret'  : '87aefb60ee574c9c9831d8ff42b308b4',
	'grant_type'     : 'authorization_code', 
	'redirect_uri'   : '',
	'auth_uri'       : 'https://api.instagram.com/oauth/authorize/',
	'token_uri'      : 'https://api.instagram.com/oauth/access_token/'
}

instagram_url = 'https://www.instagram.com'
oauth_base_url = 'https://api.instagram.com/oauth'




#builds the authorization url
def auth_url():
        data = {
            'client_id': client['client_id'],
            'redirect_uri': client['redirect_uri'],
            'response_type': 'code',
            'scope': ' '.join(None or [])
        }
        url = '%s/authorize' % oauth_base_url
        req = requests.Request('GET', url, params=data)
        prepared = req.prepare()
        return prepared.url
    
    
def get_browser_auth_url(authurl):
    req = requests.get(authurl)
    redirected_to = req.url
    return redirected_to
        

#Send a request to obtain an access token.
def exchange_code_for_accesstoken(code):
    data = {
        'code': code,
        'client_id': client['client_id'],
        'client_secret': client['client_secret'],
        'redirect_uri': client['redirect_uri'],
        'grant_type': client['grant_type']
    }
    req = requests.post('%s/access_token' % oauth_base_url, data=data)
    result = req.json()
    return result


if __name__ == "__main__":
    import json

    raw_scope = ''
    scope = raw_scope.split(' ')

    url = auth_url()
    print ("Visit this page and grant access: %s" % url)

    code = 'code'
    result = exchange_code_for_accesstoken(code)
    print (result)
    print ("\nSuccess!\nAccess token: %s\nUser: %s" % (result['access_token'], json.dumps(result['user'], indent=2)))
    
    
    