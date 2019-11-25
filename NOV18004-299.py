import json
import requests

Zoho_basedUrl= "https://crm.zoho.com/crm/private/json/"
from datetime import datetime, timedelta
ZOHO_TOKEN = '4c294a48a4a923e5e73f303987f0f248'
class Zohocrm(object):
    def get_records(self, module_name, start_record="1", end_record="200"):
        api_url = "https://crm.zoho.com/crm/private/json/" + module_name + "/getRecords?authtoken=" + ZOHO_TOKEN + "&scope=crmapi&fromIndex=" + str(
            start_record) + "&toIndex=" + str(end_record)
        print(api_url)
        #    API_HEADERS = {
        #        "Authorization": "Zoho-oauthtoken "+ZOHO_TOKEN
        #    }
        # GET Request
        request_response = requests.get(
            url=api_url
        )
        print(json.dumps(json.loads(request_response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        json_response = json.loads(request_response.text)
        return json_response

    # def update_record(self, module_id, module_name, value, content, zoho_method):
    #     xmldata = "<" + module_name + "><row no=\"1\"><FL val=\"" + value + "\">" + str(
    #         content) + "</FL></row></" + module_name + ">"
    #     api_url = Zoho_basedUrl + module_name + "/" + zoho_method + "?authtoken=" + ZOHO_TOKEN + "&scope=crmapi&id=" + str(
    #         module_id) + "&xmlData=" + str(xmldata)
    #     request_response = requests.post(
    #         url=api_url
    #     )
    #     json_response = json.loads(request_response.text)
    #     print(json.dumps(json.loads(request_response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    #     return json_response

ZohoObj=Zohocrm()
record_module_name = 'Contacts'
ZohoObj.get_records(record_module_name)