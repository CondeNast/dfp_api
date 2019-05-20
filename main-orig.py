# Import the library.
from googleads import ad_manager

# Initialize a client object, by default uses the credentials in ~/googleads.yaml.
client = ad_manager.AdManagerClient.LoadFromStorage()

# Initialize a service.
network_service = client.GetService('NetworkService', version='v201902')

# Make a request.
current_network = network_service.getCurrentNetwork()

print 'Found network %s (%s)!' % (current_network['displayName'],
                                  current_network['networkCode'])

audience_segment_service = client.GetService('AudienceSegmentService', version='v201902')

  
# Get the root ad unit ID used to target the entire network.
root_ad_unit_id = (
    network_service.getCurrentNetwork()['effectiveRootAdUnitId'])

# Create inventory targeting (pointed at root ad unit i.e. the whole network)
inventory_targeting = {
    'targetedAdUnits': [
        {'adUnitId': root_ad_unit_id}
    ]
}

# Create custom criteria.
custom_criteria = [
  {
      'xsi_type': 'CustomCriteria',
      'keyId': '11772758',
      'valueIds': ['448115859104'],
      'operator': 'IS'
  }
]

# Create the custom criteria set.
top_custom_criteria_set = {
  'logicalOperator': 'AND',
  'children': custom_criteria
}

# Create the audience segment rule.
rule = {
 'inventoryRule': inventory_targeting,
 'customCriteriaRule': top_custom_criteria_set
}


# Create an audience segment.
audience_segment = [
  {
      'xsi_type': 'RuleBasedFirstPartyAudienceSegment',
      'name': 'Test SG - Spire Shadow z8lkqp',
      'description': 'Spire > Home > In-Market > Mattress',
      'pageViews': '1',
      'recencyDays': '1',
      'membershipExpirationDays': '7',
      'rule': rule
  }
]

audience_segments = (
    audience_segment_service.createAudienceSegments(audience_segment))

for created_audience_segment in audience_segments:
    print ('An audience segment with ID "%s", name "%s", and type "%s" '
        'was created.' % (created_audience_segment['id'],
            created_audience_segment['name'],
            created_audience_segment['type']))
