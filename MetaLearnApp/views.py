from web3 import Web3
from django.conf import settings

web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER_URL))


# Check connection
if web3.is_connected():
    print("Connected to blockchain")
else:
    print("Failed to connect")
