#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python example script showing proper use of the Cisco Sample Code header.

Copyright (c) 2023 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""


from __future__ import absolute_import, division, print_function


__author__ = "Russell Johnston <rujohns2@cisco.com>"
# __contributors__ = [
#     "Arthur Dent <arthurde@cisco.com>",
#     "Ford Prefect <fordpref@cisco.com>",
#     "Slartibartfast <slartiba@cisco.com>",
# ]
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import argparse
import xmltodict
from virl2_client import ClientLibrary

parser = argparse.ArgumentParser(description="Provide file location of session.xml")
parser.add_argument(
    "file_path",
    type=str,
    help="Provides the location of the session.xml file",
)
args = parser.parse_args()

# Get Session Details to start appropriate CML Lab
with open(args.file_path) as f:
    session_info = xmltodict.parse(f.read())

cml_lab = session_info["session"]["scenario"]["name"]

# Connect to CML using Environment Variables for Authentication
# VIRL2_URL, VIRL2_USER and VIRL2_PASS
client = ClientLibrary(ssl_verify=False)

lab = client.find_labs_by_title(cml_lab)[0]

# If lab is not started start the lab once lab is in started state notify user of Started state.
if lab.state() != "STARTED":
    print(
        f"CML Lab: {lab._title} is Starting please standby, this can take several minutes to complete."
    )
    lab.start()
    # After Lab starts

print(f"CML Lab: {lab._title} is {lab.state()}")
