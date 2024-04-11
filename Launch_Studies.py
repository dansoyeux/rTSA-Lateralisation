# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:35:53 2023

@author: user
"""

from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random, Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)
from anypytools import AnyPyProcess

from anypytools import AnyMacro

import numpy as np

import os

# %% nombre de simulation en parallèle

num_processes = 5

# %% Paramètres mouvement et modèle

MovementType_list = ["CoronalElevation", "ScapularElevation", "SagitalElevation"]

# %% Cas de simulation

glenoid_lateralisation_offset_list = [-10, -5, 0, 5]
glenoid_superior_offset_list = [-6, -4, -2, 0]
humeral_lateralisation_list = [0, 5, 10, 15]

# %% Script lancement simulation

macrolist = []

for MovementType in MovementType_list:

    for glenoid_medial_offset in glenoid_medial_offset_list:

        for glenoid_superior_offset in glenoid_superior_offset_list:

            ResultFileName = f"{MovementType}_IS_{glenoid_superior_offset}_ML_{glenoid_medial_offset}"

            macrolist.append([
                Load('rTSA-Lateralisation.main.any',
                     defs={'MovementType': f"{MovementType}",
                           'ResultFileName': f'"{ResultFileName}"',
                           'glenoid_anteriorisation': 0,
                           'glenoid_distalisation': glenoid_superior_offset,
                           'glenoid_medialisation': glenoid_medial_offset,
                           'humeral_lateralisation': glenoid_medial_offset,
                           'rTSA': 1,
                           'GHReactionsOn': 0,
                           'AutoSaveOption': 1,
                           },  # fin defs
                     ),  # fin Load
                OperationRun('Main.RunApplication')
            ])


# %% Launch study without timeout

app = AnyPyProcess(timeout=3600 * 100, num_processes=num_processes,
                   anybodycon_path=r"C:\Users\user\AppData\Local\Programs\AnyBody Technology\AnyBody.8.0\anybodycon.exe")
app.start_macro(macrolist)
