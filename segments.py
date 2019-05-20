#!/usr/bin/env python
#
# Copyright 2015 Google Inc. All Rights Reserved.
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

"""This example creates a new rule based first party audience segment."""

import uuid
import sys

# Import appropriate modules from the client library.
from googleads import ad_manager

def main(arg1, argv):
  action = arg1
  seg_ids = ",".join(argv)
  
  xsi_type = None
  if action in ['pop', 'populate']:
    xsi_type = 'PopulateAudienceSegments'
  elif action in ['act', 'activate']:
    xsi_type = 'ActivateAudienceSegments'
  elif action in ['deac', 'deactivate']:
    xsi_type = 'DeactivateAudienceSegments'
  else:    
    print 'Unrecognized Action'
    return

  # Initialize a client object, by default uses the credentials in ~/googleads.yaml.
  client = ad_manager.AdManagerClient.LoadFromStorage()

  # Initialize appropriate services.
  audience_segment_service = client.GetService(
      'AudienceSegmentService', version='v201902')
  
    # Create statement object to get the specified first party audience segment.
  statement = (ad_manager.StatementBuilder(version='v201902')
               .Where('Type = :type AND Id IN (%s)' % seg_ids)
               .WithBindVariable('type', 'FIRST_PARTY')
               .Limit(10))

  response = audience_segment_service.getAudienceSegmentsByStatement(
      statement.ToStatement())

  if 'results' in response and len(response['results']):
    segments = response['results']

    action = {
        'xsi_type': xsi_type
    }
    
    for segment in segments:
      print (
          'Working on audience segment with id "%s" and name "%s"'
          % (segment['id'], segment['name']))

    populated_audience_segments = (
        audience_segment_service.performAudienceSegmentAction(
            action, statement.ToStatement()))

    print ('%s audience segment changed ' %
           populated_audience_segments['numChanges'])
  else:
    print 'No segments found'


if __name__ == "__main__":
  if (len(sys.argv) < 3):
    print 'Usage: segments action segment_ids'
  else:
    main(sys.argv[1],sys.argv[2:])
