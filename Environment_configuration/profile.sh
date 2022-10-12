#!/bin/bash

## Copyright (c) Microsoft. All rights reserved.
## Licensed under the MIT license. See LICENSE file in the project root for full license information.

export sub_id="<<your-subscription-id>>"
export rg_name="<<your-resource-name>>"
export base_type="Microsoft.EventGrid/namespaces"
export ns_id_prefix="/subscriptions/${sub_id}/resourceGroups/${rg_name}/providers/Microsoft.EventGrid/namespaces"

echo "Namespace prefix set to ${ns_id_prefix}"