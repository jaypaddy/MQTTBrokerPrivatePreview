# Copyright (c) Microsoft Corporation. All rights reserved.S
# Licensed under the MIT License. See License.txt in the project root for
# license information.
import os
import sys
import logging  # noqa: F401
import json
import time
from paho_client import PahoClient
from dotenv import load_dotenv
load_dotenv()

"""
Uncomment the following lines to enable debug logging
"""
# logging.basicConfig(level=logging.INFO)
# logging.getLogger("paho").setLevel(level=logging.DEBUG)
envseq="0_"

client_id = os.getenv("{}PUB_CLIENT_ID".format(envseq))
#print(client_id)
gw_url = os.getenv("GW_NS_URL")
#print(gw_url)

payload = {"seq": 1, "latitude": 47.63962283908785, "longitude": -122.12718926895407}

cert_path = os.getenv("{}PUB_CERT_PATH".format(envseq))
#../cert-gen/certs/{}.cert.pem"
cert_key_path = os.getenv("{}PUB_CERT_KEY_PATH".format(envseq))
#"../cert-gen/certs/pub-client.key.pem"
#print(cert_path)
#print(cert_key_path)
##################################
# CREATE CLIENT
##################################

client = PahoClient.create_from_x509_certificate(client_id, cert_path, cert_key_path, "1234", gw_url)

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
    
print 
##################################
# PUBLISH
##################################
#topic = "samples/topic"
topic = os.getenv("{}PUB_TOPIC".format(envseq))


for i in range(0, 20):
    client.print_msg("Publishing Message {} to {} at QOS=1".format(i,topic))
    payload["seq"] = i
    (rc, mid) = client.publish(topic, json.dumps(payload), qos=1)
    #client.print_msg("Publish returned rc={}: {}".format(rc, PahoClient.error_string(rc)))

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
