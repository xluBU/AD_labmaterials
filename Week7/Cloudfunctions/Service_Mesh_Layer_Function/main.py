# start imports
import requests
import json

# end imports

# Service Cloud function to get a list of inventory items
# the passed request object should contain the url of the mesh service to use.
def services_get_inventory_list_file(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    # check to see which data source to use and switch to the approrpiate mesh service.
    if(request_json and 'source' in request_json):
        # if JSON passed - use API tester to test
        meshSource = request_json['source']
    else:
        # if querystring passed - helps with testing quickly
        meshSource = request.args.get("source")
    # print(request.args.get("source"))
    # naive implementation - as code will need updating to add/edit meshSources. What would be a better way to implement this?
    if(meshSource=="mongo"):
        url = 'https://europe-west2-ad-labs-328821.cloudfunctions.net/display_mongoDB'
    else:
        url = "https://europe-west2-ad-labs-328821.cloudfunctions.net/GoogleStorage_Display"
    # get the data
    json_data = requests.get(url).content
    # return the data
    return json_data