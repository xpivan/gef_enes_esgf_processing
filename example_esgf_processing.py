#!/usr/bin/env python3
#
# Example of processing a time average calculation using icclim on an NetCDF file

import os
import requests
import tempfile
import argparse
import gef_enes_esgf_processing

parser = argparse.ArgumentParser()
parser.add_argument("-key", "--api_key", help="Provide api_key to ESGF CWT",
                    type=str)
args = parser.parse_args()
api_key = args.api_key

gef_enes_esgf_processing.netcdf_processing("processing_params.json", api_key)
