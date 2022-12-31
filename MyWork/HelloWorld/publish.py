# Copyright (c) Microsoft Corporation. All rights reserved.S
# Licensed under the MIT License. See License.txt in the project root for
# license information.
import os
import sys
import logging  # noqa: F401
import json
import time
from paho_client import PahoClient

"""
Uncomment the following lines to enable debug logging
"""
# logging.basicConfig(level=logging.INFO)
# logging.getLogger("paho").setLevel(level=logging.DEBUG)

client_id = "asset1-pub"
gw_url = "mqtteventgridns.centraluseuap-1.ts.eventgrid.azure.net"



##################################
# CREATE CLIENT
##################################
cert_path = "../Certs/pub-client1.cert.pem"
cert_key_path = "../Certs/pub-client1.key.pem"

client = PahoClient.create_from_x509_certificate(client_id, cert_path, cert_key_path, "1234", gw_url, clean_session=True)


##################################
# CONNECT
##################################

client.print_msg("Connecting...")
client.start_connect()

if not client.connection_status.wait_for_connected(timeout=20):
    client.print_msg("Failed to connect. Exiting")
    sys.exit(1)
client.print_msg("Connected")
print()

##################################
# PUBLISH
##################################
topic = "assets/{}/basic".format(client.auth.device_id)
payload = {"humidity": 47.63962283908785, "temp": 80.12718926895407}

client.print_msg("Publishing to {} at QOS=1".format(topic))
(rc, mid) = client.publish(topic, json.dumps(payload), qos=1)
client.print_msg("Publish returned rc={}: {}".format(rc, PahoClient.error_string(rc)))

client.print_msg("Waiting for PUBACK for mid={}".format(mid))
if client.incoming_pubacks.wait_for_ack(mid, timeout=20):
    client.print_msg("PUBACK received")
else:
    client.print_msg("PUBACK not received within 20 seconds")
print()

##################################
# DISCONNECT
##################################

time.sleep(1)
client.print_msg("Disconnecting")
client.disconnect()
client.connection_status.wait_for_disconnected()
