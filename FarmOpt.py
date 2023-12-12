"""
########################################################################################################################
# Farm Optimizer
#
# Version 0.1 Alpha
#
# This library has all the functions and objects for optimizing crop rotation and grants
#
#
#
# Developed by: George Crossley, and Ajit C Pillai
# Contact: ajit.c.pillai@gmail.com
# Last Updated: 2023-12-12
########################################################################################################################
"""

import os
import numpy as np
import pandas as pd

class Farm:
    def __init__(self, fpath, length, width):
        """

        :param fpath:
        """

        self.fields = []

        with open(fpath, 'r') as f:
            field_data = pd.read_csv(f)

        for field in field_data:
            self.fields.append(Field(field))

class Field:
    """

    """

    def __init__(self, field_data):
        """

        :param field_data:
        """

        # Field Definitions
        self.name = []
        self.number = []
        self.area = []
        self.slope = False
        self.runoff = False

        # Field State Parameters
        self.crop = []
        self.subsidy = []
        self.nitrogen = []






