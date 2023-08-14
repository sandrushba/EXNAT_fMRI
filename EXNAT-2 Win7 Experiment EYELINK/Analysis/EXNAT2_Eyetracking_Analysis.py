#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:05:29 2023

@author: merle
"""


# Okay so for some reason, all Eyelink EDFs are not saved as 
# regular EDFs but in a weird Eyelink format. So they have to 
# be converted to .asc format using Eyelink's EDFConverter app.


import os
os.chdir('/Volumes/MERLE 1/EXNAT-2/EEG_study_EXNAT2/EXNAT-2 Win7 Experiment EYELINK/Analysis/')

# import function to read in those weird asc files as pandas df
from ParseEyeLinkAsc import * 

import pandas as pd


test = ParseEyeLinkAsc("test.asc")
