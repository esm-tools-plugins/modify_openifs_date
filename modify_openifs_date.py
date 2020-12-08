import os

def modify_openifs_date(config):
    pp_method = pp_type = None
    for model in config["general"]["valid_model_names"]:
        if "modify_openifs_date" in config[model]:
            for name in config[model]["modify_openifs_date"]:
                if "method" in config[model]["modify_openifs_date"][name]:
                    pp_method = config[model]["modify_openifs_date"][name]["method"]
                if "type" in config[model]["modify_openifs_date"][name]:
                    pp_type = config[model]["modify_openifs_date"][name]["type"]
                if pp_type == "shell" and pp_method:
                    #try:
                    os.system(pp_method)
                    #except:
                    #    print("Shell execution of command: '" + pp_method + "' failed, please check...")
    return config
                
