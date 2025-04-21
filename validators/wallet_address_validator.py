from abc import ABC
import re

from jsonschema import ValidationError



class WalletAddressValidator(ABC): 

   def validateWalletAddress(value: str):
       if not re.fullmatch(r"0x[a-fA-F0-9]{40}", value): raise ValidationError("Invalid Ethereum address format.")