import json
import requests
from .StringHelper import StringHelper


class IpfsHelper:

    '''
        API Key: 6505b764c0744df21f9b
        API Secret: 350ca3f44ff53f0637731ba34c585600493d42bf999a3f31fa229cd860366582
        JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI4OGI1NmU1NC1hNzAxLTRhZGUtYmQwNS04NWMzMDM2ZTM2MGMiLCJlbWFpbCI6ImFvdWxlZGlzc2F5b3VzcmlAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9LHsiaWQiOiJOWUMxIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjY1MDViNzY0YzA3NDRkZjIxZjliIiwic2NvcGVkS2V5U2VjcmV0IjoiMzUwY2EzZjQ0ZmY1M2YwNjM3NzMxYmEzNGM1ODU2MDA0OTNkNDJiZjk5OWEzZjMxZmEyMjljZDg2MDM2NjU4MiIsImlhdCI6MTcwMDM0MzA3NX0.soJI0AFpmATe429yyCdvKipb_jmvHMBbvE38TWPHQ-o
    '''

    __URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    __JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI1YzczNjY3Ny0yNWQ3LTQzM2EtYjMyNS0yNDhiOTIxM2RhMzYiLCJlbWFpbCI6ImFja2VybWFubGV2aTE4M0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJpZCI6IkZSQTEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX0seyJpZCI6Ik5ZQzEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiOGU4YmRmMTczYmJjYTNhMjNjMjQiLCJzY29wZWRLZXlTZWNyZXQiOiI5NTM4YTBkZmIwNjAyMjg4ZGI0ZjZkYTAyYWUyYjcxOGRhN2JmMjEyMjNiYmI2YjczNjc4ZDUwZWM3ZWRkYjQ3IiwiaWF0IjoxNzAxMDM1MDE3fQ._obpg_mZNhoNEMqyLZ3egmq9t0iuDjwZbbM-GMJ9Tb4"
    __GATEWAY_URL = "https://green-genetic-coyote-962.mypinata.cloud/ipfs/"

    @staticmethod
    def uploadData(data):
        return json.loads(
            requests.post(
                IpfsHelper.__URL, 

                json={
                    "pinataContent" : data,
                    "pinataMetadata": { "name": StringHelper.generateRandomString() }
                },

                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "authorization": f"Bearer {IpfsHelper.__JWT}"
                }
            ).text
        )
    
    @staticmethod
    def fetchData(cid: str):
        return json.loads(requests.get(f"{IpfsHelper.__GATEWAY_URL}{cid}").text)

        