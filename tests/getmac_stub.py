"""Stub for the getmac library.

Extremely simple stub for the getmac library. A lot of
assumptions here:

  * Only supports "from getmac import get_mac_address"
  * Will return hardcoded MACs for some IPs
  * Returns None for unmatched addresses

"""
from pyatv import exceptions


IP = '127.0.0.1'
MAC = 'aa:bb:cc:dd:ee:ff'
IP_UNKNOWN = '127.0.0.2'
IP_EXCEPTION = '127.0.0.3'


def stub(module, mapping=None):
    """Stub a module using getmac."""
    def get_mac_address_stub(ip=None, network_request=True):
        if ip == IP:
            return MAC
        if mapping is not None and ip in mapping:
            return mapping[ip]
        if ip == IP_EXCEPTION:
            raise exceptions.DeviceIdUnknownError('error')
        return None

    module.get_mac_address = get_mac_address_stub
