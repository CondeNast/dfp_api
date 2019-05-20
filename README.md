# dfp_api
Sample scripts for manipulating audience segments on Google Ad Manager (formerly DFP API)

## Pre-requisites
1. Python 2.7
2. A configration file called googleads.yaml in the users's home directory containing authentication information, the layout of the file is described in detail at https://github.com/googleads/googleads-python-lib/blob/master/googleads.yaml under section AdManagerClient
3. Install the googleads library based on instructions described in https://github.com/googleads/googleads-python-lib

### Key Scripts

1. Create a new segment

```
python create_segment.py name systemcode

Where, 
  name = Name of the new segment
  systemcode = System code associated with the the segment on the segmentation platform
```

2. Rename a segment

```
python rename_segment.py oldname newname

Where, 
  oldname = Current name of the segment
  newname = New name of the segment
```

3. Activate, Deactivate or Populate

```
python segments.py action segment-id1 [segment-id2 .. segment-idN]

Where, 
  action = act OR activate for activating
         | deac OR deactivate for deactivating
         | pop OR populate for populating           
  segment-id1 ... N = List of segment IDs
```


