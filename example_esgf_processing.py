#!/usr/bin/env python3
#
# Example of processing a time average calculation using icclim on an NetCDF file

import os
import requests
import tempfile
import argparse
import gef_enes_esgf_processing

parser = argparse.ArgumentParser()
parser.add_argument("-key", "--api_key", help="provide api_key to ESGF CWT",
                    type=str)
args = parser.parse_args()
api_key = args.api_key

object_url = 'http://www.cerfacs.fr/~page/psl_Amon_CNRM-CM5_rcp45_r1i1p2_200601-203512.nc'
output_file = 'out.nc'

response = requests.get(object_url, stream=True)

# Throw an error for bad status codes
response.raise_for_status()

with tempfile.NamedTemporaryFile(delete=False) as handle:
    for block in response.iter_content(1024):
        handle.write(block)

gef_enes_esgf_processing.netcdf_processing(handle.name, "processing_params.json", api_key, output_file)

os.unlink(handle.name)
