from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('XPEogtPJlI-nFOgktavXytmNJVO5ddUIdQeKT20VZ_6r')
discovery = DiscoveryV1(
    version='{version}',
    authenticator=authenticator
)

discovery.set_service_url('https://api.us-east.discovery.watson.cloud.ibm.com/instances/f5edcf88-08d9-4afc-af95-58c158f3021d')
