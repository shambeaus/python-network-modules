
import re
from ciscoconfparse import CiscoConfParse
import pprint

# function to parse through object and object-group configuration on ASA firewalls
# returns a dictionary of configured members of groups

object_regex = re.compile(r'object network [\w\-]+')
object_group_regex = re.compile(r'object-group network [\w\-]+')
ip_regex = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")


def listNetObject(sh_run):
    #Get list of all object-netwoks
    net_object_list = {}
    parse = CiscoConfParse(sh_run)
    objectList = parse.find_objects(r'object network [\w\-]+')
    for line in objectList:
        if line.re_search_children(r'((host)|(subnet)) [\w\.]+'):
            obj_name = re.search(r'object network ([\w\-]+)',line.text).group(1)
            host = line.re_search_children(r'((host)|(subnet)) ([\w\.]+)')[0].text
            net_object_list[obj_name] = host
    return net_object_list


def listGroupChildren(sh_run):
    object_group_list = {}
    obj_group = []
    parse = CiscoConfParse(sh_run)
    group_list = parse.find_objects(object_group_regex)
    for line in group_list:
        group_name = re.search(r'object-group network ([\w\-]+)',line.text).group(1)
        group_child = line.re_search_children(r'(network-object [\w\-]+)|(group-object [\w\-]+)')
        for line in group_child:
            if re.search(r'group-object ([\w\-\.]+)', line.text):
                val = re.search(r'group-object ([\w\-\.]+)', line.text).group(1)
                obj_group.append(val)
            if re.search(r'network-object (\w.+)', line.text):
                val = re.search(r'network-object (\w.+)', line.text).group(1)
                obj_group.append(val)
        object_group_list[group_name] = obj_group
        obj_group = []
    return object_group_list


object_list = listNetObject('running_config')
object_group_list = listGroupChildren('running_config')