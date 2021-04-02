#!/usr/bin/env python3

"""
  Huawei LTE modem api

  # API: https://github.com/Salamek/huawei-lte-api
  pip install huawei-lte-api

  export ADMIN_PASSWORD="<pass>"
  huawei-lte.py [enable|disable]

"""

import os
import sys

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection


def main(argv):
  """
  toggle LTE modem state

  :param dataswitch: 0 to disable LTE modem, 1 to enable LTE modem
  """

  admin_password = os.environ.get("ADMIN_PASSWORD")
  connection = AuthorizedConnection('http://192.168.8.1/',
                                    username='admin',
                                    password=admin_password)

  client = Client(connection)

  if len(argv) == 2:
    if argv[1] == "enable":
      client.dial_up.set_mobile_dataswitch(1)
    elif argv[1] == "disable":
      client.dial_up.set_mobile_dataswitch(0)
    else:
      sys.exit("ERROR: unknown parameter")
  else:
    # print status
    status = client.dial_up.mobile_dataswitch()
    if int(status['dataswitch']) == 0:
      print('status: disabled')
    else:
      print('status: enabled')


if __name__ == "__main__":
  main(sys.argv)
