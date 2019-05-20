#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example gets all custom targeting keys and values.
"""

# Import appropriate modules from the client library.
import sys

from googleads import ad_manager
CUSTOM_TARGETING_KEY_ID = '11772758'

def main(client, key_id, value, name=''):
  # Initialize appropriate service.
  custom_targeting_service = client.GetService(
      'CustomTargetingService', version='v201902')

  # Create a statement to select custom targeting values.
  statement = (ad_manager.StatementBuilder(version='v201902')
               .Where("customTargetingKeyId = %s AND name = '%s'" % (key_id, value)))

  # Retrieve a small amount of custom targeting values at a time, paging
  # through until all custom targeting values have been retrieved.
  while True:
    response = custom_targeting_service.getCustomTargetingValuesByStatement(
        statement.ToStatement())

    if 'results' in response and len(response['results']):
      for custom_targeting_value in response['results']:
        # Print out some information for each custom targeting value.
        print('Custom targeting value with ID "%d", name "%s", display name '
              '"%s", and custom targeting key ID "%d" was found.\n' %
              (custom_targeting_value['id'], custom_targeting_value['name'],
               custom_targeting_value['displayName'],
               custom_targeting_value['customTargetingKeyId']))
      statement.offset += statement.limit
      return custom_targeting_value['id']
    else:
      # Create this new value and then return the value ID back
      # Create custom targeting value objects.
      values = [
          {
              'customTargetingKeyId': key_id,
              'displayName': name,
              'name': value,
              'matchType': 'EXACT'
          }
      ]

      # Add custom targeting values.
      values = custom_targeting_service.createCustomTargetingValues(values)

      # Display results.
      if values:
        for value in values:
          print ('A custom targeting value with id "%s", belonging to key with id'
                 ' "%s", name "%s", and display name "%s" was created.'
                 % (value['id'], value['customTargetingKeyId'], value['name'],
                    value['displayName']))
          return value['id']
      else:
        print 'No values were created.'
        return -1

    break

if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  main(ad_manager_client, CUSTOM_TARGETING_KEY_ID, *sys.argv[1:])
