from ciscoconfparse import CiscoConfParse


def remove_config_blocks(run_config):

    parse = CiscoConfParse(run_config)
    # delete exiting configuration that needs to be replaced
    for obj in parse.find_objects(r"^interface"):
        obj.delete()
    for obj in parse.find_objects(r"boot system"):
        obj.delete()

    # commit modifications to the current parse object
    parse.commit()

    #return IOS formated config to be used in script

    return '\n'.join(parse.ioscfg)
    # use below parse command if file needs to be saved locally
    # parse.save_as('modified_startup')