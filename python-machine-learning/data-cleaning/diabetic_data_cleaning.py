# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

filename = 'diabetic_data.csv'
names = [
    'encounter_id', 'patient_nbr', 'race', 'gender', 'age', 'weight',
    'admission_type_id', 'discharge_disposition_id', 'admission_source_id',
    'time_in_hospital', 'payer_code', 'medical_specialty',
    'num_lab_procedures', 'num_procedures', 'num_medications',
    'number_outpatient', 'number_emergency', 'number_inpatient', 'diag_1',
    'diag_2', 'diag_3', 'number_diagnoses', 'max_glu_serum', 'A1Cresult',
    'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride',
    'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone',
    'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'tolazamide',
    'examide', 'citoglipton', 'insulin', 'glyburide-metformin',
    'glipizide-metformin', 'glimepiride-pioglitazone',
    'metformin-rosiglitazone', 'metformin-pioglitazone', 'change',
    'diabetesMed', 'readmitted'
]
data = pd.read_csv(filename, names=names, low_memory=False)
# print(data)

# ===================================Using NumPy===============================
# import numpy as np
#
# filename = 'diabetic_data.csv'
# raw_data = open(filename,'rt')
# np_data = np.loadtxt(raw_data, delimiter=",")
# print(np_data)
# =============================================================================

# =========================Using standard lib==================================
# import csv
# import numpy as np
# 
# filename = 'diabetic_data.csv'
# raw_data = open(filename, 'rt')
# reader = csv.reader(raw_data, delimiter=",", quoting=csv.QUOTE_NONE)
# x = list(reader)
# data = np.array(x) #.astype('float')
# print(data)
# =============================================================================
