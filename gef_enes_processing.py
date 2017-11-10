# -*- coding: latin-1 -*-

#  Copyright CERFACS (http://cerfacs.fr/)
#  Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
#
#  Author: Christian Page (2017)

import json
from icclim import *
import datetime
from icclim.util import callback

def netcdf_processing(in_file,
                      params_file,
                      out_file
                      ):

# Extract parameters for processing
    with open(params_file) as data_file:    
        plist = json.load(data_file)

# Extract processing function parameters
    var_name = plist["function"]["var_name"]
    out_var_name = plist["function"]["out_var_name"]
    slice_mode = plist["function"]["slice_mode"]
    if slice_mode == "None": slice_mode = None

    if plist["function"]["calc_operation"] == "time_avg":
        my_indice_params = {'indice_name': out_var_name, 
                            'calc_operation': 'mean'
                            }
    else:
        raise ValueError('Operation specified in calc_operation is not implemented: '+plist["function"]["calc_operation"])
        
    dd_b, mm_b, yyyy_b = map(int, plist["function"]["time_range_b"].split('-'))
    dd_e, mm_e, yyyy_e = map(int, plist["function"]["time_range_e"].split('-'))
        
    period = [datetime.datetime(yyyy_b,mm_b,dd_b), datetime.datetime(yyyy_e,mm_e,dd_e)]

# Launch processing using icclim
    icclim.indice(user_indice=my_indice_params, in_files=in_file, var_name=var_name, slice_mode=slice_mode, base_period_time_range=period, out_unit='days', out_file=out_file, callback=callback.defaultCallback2)
