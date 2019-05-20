# Import the library.
import sys

from googleads import ad_manager
import create_audience_segments
import get_valueid_forvalue

# Set the IDs of the custom criteria to be used in the segment rule.
CUSTOM_TARGETING_KEY_ID = '11772758'    #vnd_4d_sg
CUSTOM_NAME_SUFFIX      = ' (4D)'

#CUSTOM_TARGETING_VALUE_ID = 'INSERT_CUSTOM_TARGETING_VALUE_ID_HERE'

def main(name, value=None):
    # Initialize a client object, by default uses the credentials in ~/googleads.yaml.
    client = ad_manager.AdManagerClient.LoadFromStorage()

    # Initialize a service.
    network_service = client.GetService('NetworkService', version='v201902')
    
    # Make a request.
    current_network = network_service.getCurrentNetwork()
    print 'Connected to network %s (%s)!' % (current_network['displayName'],
                                  current_network['networkCode'])

    # More logic to convert value name to value id

    # Creating new audience segment
    print "Creating new audience segment called " + name

    if (value):
        value_id = get_valueid_forvalue.main(client, CUSTOM_TARGETING_KEY_ID, value)
        create_audience_segments.main(client, name + CUSTOM_NAME_SUFFIX, CUSTOM_TARGETING_KEY_ID, value_id)
    else:
        # Create an audience segments with no KV conditions
        create_audience_segments.main(client, name + CUSTOM_NAME_SUFFIX)
    
if __name__ == "__main__":
  numargs = len(sys.argv)
  if (numargs in [2,3]):
    main(*sys.argv[1:])
  else:  
    print 'Usage: create_segment segname [systemcode]'
  