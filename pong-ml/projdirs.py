'''
projdirs.py

The directory structure of the project.
'''

import os

working_dir = os.path.dirname(os.path.realpath(__file__))

data = os.path.join(working_dir, 'collected_data')
data_special = os.path.join(data, 'special')
data_special_ideal = os.path.join(data, 'special', 'ideal')
