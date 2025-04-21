

from abc import ABC
import re

from jsonschema import ValidationError


class IpfsValidator(ABC):

    @staticmethod
    def validateCID(value):
        if not re.match(r'^[A-Za-z0-9]{46}$', value): raise ValidationError(f"{value} is not a valid IPFS CID.")