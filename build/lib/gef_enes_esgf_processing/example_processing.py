#!/usr/bin/env python3
#
# Example of processing a time average calculation using icclim on an NetCDF file

import os
import requests
import tempfile
import gef_enes_processing

object_url = 'http://www.cerfacs.fr/~page/psl_Amon_CNRM-CM5_rcp45_r1i1p2_200601-203512.nc'
output_file = 'out.nc'

response = requests.get(object_url, stream=True)

# Throw an error for bad status codes
response.raise_for_status()

with tempfile.NamedTemporaryFile(delete=False) as handle:
    for block in response.iter_content(1024):
        handle.write(block)

gef_enes_processing.netcdf_processing(handle.name, "processing_params.json", output_file)

os.unlink(handle.name)
