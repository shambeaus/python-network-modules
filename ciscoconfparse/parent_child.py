from ciscoconfparse import CiscoConfParse

# Example using the childspec functionality to find interfaces that are not shutdown

def find_active_interfaces(file):
    all_interfaces = []
    # Parser set to look at running config
    parse = CiscoConfParse(file)
    retval = ''
    # find objects matching interface and not shutdown
    for obj in parse.find_objects_wo_child(parentspec=r"^interface", childspec=r"shutdown"):
        # Make a list that will contain the parent and the children
        interface_list = []
        # Add the parent to the list as a string
        interface_list.append(obj.text)
        retval += obj.text + '\n'
        # For all the parent's children
        for line in obj.all_children:
            # Add the child to the list as a string
            retval += line.text + '\n'
        # A
    return retval


def print_config(interface_list):
    for interface in interface_list:
        for line in interface:
            print(line)


print_config(find_active_interfaces('running_config'))