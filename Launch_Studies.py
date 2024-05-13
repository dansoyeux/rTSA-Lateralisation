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

num_processes = 6

MuscleRecruitmentType = "MR_Polynomial"

# MuscleRecruitmentType = "MR_MinMaxStrict"

# %% Paramètres mouvement et modèle

MovementType_list = ["CoronalElevation", "ScapularElevation", "SagitalElevation"]

# %% Cas de simulation

# glenoid_lateralisation_offset_list = [-10, -5, 0, 5]
# glenoid_superior_offset_list = [-6, -4, -2, 0]
# humeral_lateral_offset_list = [0, 5, 10, 15]

glenoid_lateralisation_offset_list = [-10, 5]
glenoid_superior_offset_list = [-6, 0]
humeral_lateral_offset_list = [0, 15]

GHReactionsOn = 0

ResultFolderName = "Results"

# %% Script lancement simulation

macrolist = []

for MovementType in MovementType_list:
    for humeral_lateral_offset in humeral_lateral_offset_list:
        for glenoid_lateral_offset in glenoid_lateralisation_offset_list:

            for glenoid_superior_offset in glenoid_superior_offset_list:

                ResultFileName = f"{MovementType}_humLat_{humeral_lateral_offset}_glenLat_{glenoid_lateral_offset}_glenSup_{glenoid_superior_offset}"

                if MuscleRecruitmentType == "MR_MinMaxStrict":
                    ResultFileName = "MinMax_Strict_" + ResultFileName

                if GHReactionsOn == 1:
                    ResultFileName = "GHReactions_" + ResultFileName

                macrolist.append([
                    Load('rTSA-Lateralisation.main.any',
                         defs={'MovementType': f"{MovementType}",
                               'ResultFileName': f'"{ResultFileName}"',
                               'ResultFolderName': f'"{ResultFolderName}"',
                               'MuscleRecruitmentType': MuscleRecruitmentType,
                               'glenoid_anteriorisation': 0,
                               'glenoid_distalisation': glenoid_superior_offset,
                               'glenoid_lateralisation': glenoid_lateral_offset,
                               'humeral_lateralisation': humeral_lateral_offset,
                               'rTSA': 1,
                               'GHReactionsOn': GHReactionsOn,
                               'AutoSaveOption': 1,
                               },  # fin defs
                         ),  # fin Load
                    OperationRun('Main.RunApplication')
                ])

# %% Launch study without timeout

app = AnyPyProcess(timeout=3600 * 100, num_processes=num_processes, keep_logfiles=True,
                   warnings_to_include=["OBJ1",
                                        # "Penetration of surface",
                                        "Failed to resolve force-dependent kinematics"
                                        ],
                   fatal_warnings=True
                   # uncomment if on local pc
                   , anybodycon_path=r"C:\Users\user\AppData\Local\Programs\AnyBody Technology\AnyBody.8.0\anybodycon.exe"
                   )
app.start_macro(macrolist
                # , logfile="logfile"
                )
