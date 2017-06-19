import json
import requests
import argparse
import sys
import script_cod

BASE_URL = 'http://blink.devicelab.com.br'
LOGIN_URL = BASE_URL + '/signin'
DATA_MAPPING_UPDATE_URL = BASE_URL + '/application/services/datamapping/update'
TODAY_CODE = script_cod.cod_inicial()

HEADERS = {'content-type':'application/json;charset=utf-8'}

parser = argparse.ArgumentParser()
parser.add_argument("username", type=str, help="Blink username")
parser.add_argument("password", type=str, help="Blink password")

args = parser.parse_args()

CREDENTIALS = {
    "username": args.username,
    "password": args.password
    }

JSON_STR = """{
  "dataMapping": {
    "name": "codigo_inicializacao",
    "keys": [
      {
        "edit": "false",
        "value": "codigo"
      }
    ],
    "rows": [
      [
        {
          "edit": "false",
          "value": "123456"
        }
      ]
    ],
    "source": [
      {
        "codigo": "123456"
      }
    ],
    "_id": "593084ed063c467725aefaa6"
  }
}"""

DICT_DATA = json.loads(JSON_STR)

#update json code
DICT_DATA['dataMapping']['rows'][0][0]['value'] = TODAY_CODE
DICT_DATA['dataMapping']['source'][0]['codigo'] = TODAY_CODE

#s = requests.Session()
#r = s.post(LOGIN_URL, data=CREDENTIALS)

print("Logging in...")
r = requests.post(LOGIN_URL, data=CREDENTIALS)
if not 'Success' in r.text:
  print("Request error: " + r.text)
  print("Login FAIL")
  sys.exit(1)

print("Login OK")

print("Updating data-mapping")
update = requests.post(DATA_MAPPING_UPDATE_URL, headers=HEADERS, json=DICT_DATA, cookies=r.cookies)
#update = requests.post(DATA_MAPPING_UPDATE_URL, headers=HEADERS, json=DICT_DATA)

if 'blink-landing-app' in update.text:
  print("Update data mapping FAIL")
  sys.exit(1)

print("Data-mapping update SUCCESS")
print("Status Code: " + str(update.status_code))
