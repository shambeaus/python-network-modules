from ciscoconfparse import CiscoConfParse

# Example to pull config block from running config for use in scripts

def interfaces_config(run_config):
    # Extract interface config block from device
    parse = CiscoConfParse(run_config)
    retval = ''
    # find objects matching interface
    for obj in parse.find_objects(r"^interface"):
        retval += obj.text + '\n'
        for line in obj.all_children:
            # Add the child to the list as a string
            retval += line.text + '\n'
    return retval

def interfaces_config(run_config):
    # Extract interface config block from device
    parse = CiscoConfParse(run_config)
    retval = ''
    # find objects matching interface
    for obj in parse.find_objects(r"^webvpn"):
        retval += obj.text + '\n'
        for line in obj.all_children:
            # Add the child to the list as a string
            retval += line.text + '\n'
    return retval