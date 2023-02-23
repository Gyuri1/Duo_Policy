import duo_client
import json
import sys
import duo_admin_config

#new import to handle encoding
import urllib

# parsing the arg
if (len(sys.argv) != 2) :
    print("Use:")
    print(f"python {sys.argv[0]} policy_in.json")
    exit()

# reading the file
policy_filename= sys.argv[1]
print(f"Reading policy file:{policy_filename}")
try:
    f = open(policy_filename)
    policy_data = json.load(f)
    f.close()
except FileNotFoundError:
    print("File {} does not exist".format(policy_filename))
    exit()


# new function to handle post data 
def _encode_post(post_data):
  post_data_str = json.dumps(post_data)
  encoded = urllib.parse.quote_plus(post_data_str)
  post_data_outer = { 
    "payload": encoded
  }
  return post_data_outer

#  ADMIN API auth
admin_api = duo_client.Admin(ikey=duo_admin_config.ikey, skey=duo_admin_config.skey, host=duo_admin_config.api_hostname)

#  POST
test_policy_data = { "name": "new policy name", }
path = "/admin/v2/policies"
response = admin_api.json_api_call("POST", path, _encode_post(policy_data))
 
json_formatted_str = json.dumps(response, indent=2)
print(json_formatted_str)
