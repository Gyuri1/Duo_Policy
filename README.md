# Duo Policy import - export examples

Please update:  
  `duo_admin_config.py` file  -> based on Your own Duo API credentials
  
  
  
  
# How to install:

  Copy these 2 files into a working directory and make sure `requests` is an installed python library:
  
  `pip install requests` 
  
  Please install `duo_client` python package as well: 
  
  `pip install duo_client`

# How to use:

`python duo_get_policy.py >policy_out.json`

You can modify the policy_out.json file according to Your needs and save it into policy_in.json.

`python duo_post_policy.py policy_in.json`


