# -*- coding: latin-1 -*-

#  Copyright CERFACS (http://cerfacs.fr/)
#  Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
#
#  Author: Christian Page (2017)

import json
from icclim import *
import datetime
from icclim.util import callback
import cwt
import time

def netcdf_processing(params_file,
                      api_key
                      ):

# Extract parameters for processing
    with open(params_file) as data_file:    
        plist = json.load(data_file)

# Extract processing function parameters
    var_name = plist["function"]["var_name"]
    out_var_name = plist["function"]["out_var_name"]
    slice_mode = plist["function"]["slice_mode"]
    if slice_mode == "None": slice_mode = None
    in_file = plist["function"]["in_file"]
    out_file = plist["function"]["out_file"]
    esgf_cwt_wps_url = plist["function"]["esgf_cwt_wps_url"]
    try:
        geo_domain_latmin = plist["function"]["geo_domain"]["latitude"]["min"]
    except KeyError:
        geo_domain_latmin = -9999
    try:
        geo_domain_latmax = plist["function"]["geo_domain"]["latitude"]["max"]
    except KeyError:
        geo_domain_latmax = -9999
    try:
        geo_domain_lonmin = plist["function"]["geo_domain"]["longitude"]["min"]
    except KeyError:
        geo_domain_lonmin = -9999
    try:
        geo_domain_lonmax = plist["function"]["geo_domain"]["longitude"]["max"]
    except KeyError:
        geo_domain_lonmax = -9999

    if plist["function"]["calc_operation"] == "time_avg":
        my_indice_params = {'indice_name': out_var_name, 
                            'calc_operation': 'mean'
                            }
    else:
        raise ValueError('Operation specified in calc_operation is not implemented: '+plist["function"]["calc_operation"])
        
    dd_b, mm_b, yyyy_b = map(int, plist["function"]["time_range_b"].split('-'))
    dd_e, mm_e, yyyy_e = map(int, plist["function"]["time_range_e"].split('-'))
        
    period = [datetime.datetime(yyyy_b,mm_b,dd_b), datetime.datetime(yyyy_e,mm_e,dd_e)]

    if geo_domain_latmin != -9999 and geo_domain_latmax != -9999 and geo_domain_lonmin != -9999 and geo_domain_lonmax != -9999:

        # Setup ESGF CWT WPS
        wps = cwt.WPS(esgf_cwt_wps_url, api_key=api_key)

        # Get variable from in_file
        in_file_s = in_file.encode("ascii")
        var_name_s = var_name.encode("ascii")
        varproc = cwt.Variable(in_file_s, var_name_s)

        # Setup domain
        d0 = cwt.Domain([
                cwt.Dimension('time', 0, 9999999, cwt.INDICES),
                cwt.Dimension('lat', geo_domain_latmin, geo_domain_latmax),
                cwt.Dimension('lon', geo_domain_lonmin, geo_domain_lonmax),
                ])
        
        # Select gridder
        cwt.gridder.Gridder('esmf', 'linear', varproc)

        # Select processor
        proc = wps.get_process('CDAT.subset')

        # Execute processing
        wps.execute(proc, inputs=[varproc], domain=d0)

        # Check status and wait for completion
        while proc.processing:
            print proc.status
    
            time.sleep(1)
    
        # Output some feedback to user
        print proc.status

        print proc.output.uri
        print proc.output.var_name

        # Set output information
        in_file = proc.output.uri
        var_name = proc.output.var_name

    # Launch processing using icclim
    icclim.indice(user_indice=my_indice_params, in_files=in_file, var_name=var_name, slice_mode=slice_mode, base_period_time_range=period, out_unit='days', out_file=out_file, callback=callback.defaultCallback2)
