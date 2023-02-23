import duo_client
import json
import duo_admin_config

admin_api = duo_client.Admin(ikey=duo_admin_config.ikey, skey=duo_admin_config.skey, host=duo_admin_config.api_hostname)

params = {}
policies = admin_api.json_api_call('GET','/admin/v2/policies', params)
json_formatted_str = json.dumps(policies, indent=2)
print(json_formatted_str)
