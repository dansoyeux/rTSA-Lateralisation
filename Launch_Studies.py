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

medial_offset_list = [-10, -5, 0, 5]
superior_offset_list = [-6, -4, -2, 0]

# medial_offset_list = [5]
# superior_offset_list = [-2]

# %% Script lancement simulation

macrolist = []

for MovementType in MovementType_list:

    for medial_offset in medial_offset_list:

        for superior_offset in superior_offset_list:

            ResultFileName = f"{MovementType}_IS_{superior_offset}_ML_{medial_offset}"

            macrolist.append([
                Load('rTSA-Lateralisation.main.any',
                     defs={'MovementType': f"{MovementType}",
                           'ResultFileName': f'"{ResultFileName}"',
                           'anteriorisation': 0,
                           'distalisation': superior_offset,
                           'medialisation': medial_offset,
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
