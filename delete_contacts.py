import requests, json, os
from pprint import pprint


username = os.environ['OS_USERNAME']
apikey = os.environ['OS_PASSWORD']
identity_uri = os.environ['OS_AUTH_URL'] + "tokens"

customer_uri = ""

def get_rackspace_token():
    pprint(apikey)
    pprint("Getting a token =============================")
    data = { "auth":{ "RAX-KSKEY:apiKeyCredentials":{ "username":username, "apiKey":apikey } } }
    #pprint(data)
    headers = {"Content-type": "application/json"}
    r = requests.post(identity_uri, data=json.dumps(data), headers=headers)
    #pprint(r.status_code)
    #pprint(r.headers)
    #pprint(r.text)
    #r.json["access"]["serviceCatalog"]["id"]
    token = json.loads(r.content)
    #pprint(json.loads(r.content))
    token = str(token["access"]["token"]["id"])
    #pprint(token)
    return token


def get_contact_list():
	# Get list of contacts from customer
	headers = {"X-Auth-Token": token,"Accept": "application/xml"}
	r = requests.get('https://identity.api.rackspacecloud.com/v2.0/', headers=headers)
	pprint(r.status_code)
	pprint(r.headers)
	#print 'text'
	#print r.text
	print 'json'
	pprint(r.json)

pprint(get_rackspace_token())
#get_contact_list(username, token)