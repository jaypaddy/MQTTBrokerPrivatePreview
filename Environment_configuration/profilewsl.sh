#!/bin/bash

echo "Jay"
export sub_id="d0272d81-bf47-4f2b-b8dc-c56cb783e361"
export rg_name="MythicalMQTTEventGrid_RG"
export ad_username="japadman@microsoft.com" # i.e user@contoso.com
export az_region="centraluseuap"
export ns_name_suffix="mythicalmqttegns"
export base_type="Microsoft.EventGrid/namespaces"
export ns_id_prefix="/subscriptions/${sub_id}/resourceGroups/${rg_name}/providers/Microsoft.EventGrid/namespaces"

echo "Namespace prefix set to ${ns_id_prefix}"