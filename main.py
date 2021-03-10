import requests;
import urllib;
#base url, I took out trailing question mark
base_url = 'https://svcs.ebay.com/services/search/FindingService/v1?'
## parameters part 1
# add operation types
operation = 'findItemsByKeywords'

# app id is the api key
app_id = 'JosephLe-brokenRe-PRD-3dc70018e-ed3b0682'

# The format of the data sent in the response
#   Supported formats are: NV, JSON, XML
requested_data_format = 'JSON'

parameters_part1 = {
        'OPERATION-NAME': operation,
        'SERVICE-VERSION': '1.0.0',
        'SECURITY-APPNAME': app_id,
        'RESPONSE-DATA-FORMAT': requested_data_format,
        }

## parameters part 2
#keywords are what you search for
keywords = 'record players'

parameters_part2 = {
        'keywords': keywords,
        }

parameters1_url = urllib.parse.urlencode(parameters_part1)
parameters2_url = urllib.parse.urlencode(parameters_part2)
#print(parameters1_url + '&REST-PAYLOAD' + parameters2_url)
all_params = parameters1_url + '&REST-PAYLOAD' + '&' + parameters2_url
final_url = base_url + all_params
#print(final_url)
r = requests.get(final_url)
print(r.text)
