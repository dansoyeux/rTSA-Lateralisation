# import Anybody_LoadOutput.Tools as LoadOutputTools

from Anybody_Package.Anybody_LoadOutput.Tools import load_results_from_file

from Anybody_Package.Anybody_Graph.GraphFunctions import graph
from Anybody_Package.Anybody_Graph.GraphFunctions import COP_graph
from Anybody_Package.Anybody_Graph.GraphFunctions import muscle_graph
from Anybody_Package.Anybody_Graph.GraphFunctions import define_simulations_line_style
from Anybody_Package.Anybody_Graph.GraphFunctions import define_simulation_description
from Anybody_Package.Anybody_Graph.GraphFunctions import define_COP_contour

from Anybody_Package.Anybody_LoadOutput.LoadOutput import combine_simulation_cases
from Anybody_Package.Anybody_LoadOutput.LoadLiterature import load_literature_data

from Anybody_Package.Anybody_Graph import PremadeGraphs

from Anybody_Package.Anybody_Graph.Tools import save_all_active_figures

from Anybody_Package.Anybody_LoadOutput.Tools import result_dictionary_to_excel


import matplotlib

# %% Contrôle de la taille des polices des graphiques

# Titre des cases des subplots (12)
matplotlib.rcParams.update({'axes.titlesize': 18})

# Titre du graphique (12)
matplotlib.rcParams.update({'figure.titlesize': 18})

# Nom des axes (10)
matplotlib.rcParams.update({'axes.labelsize': 16})

# Graduations des axes (10)
matplotlib.rcParams.update({'xtick.labelsize': 14})
matplotlib.rcParams.update({'ytick.labelsize': 14})

# Taille des graduations (3.5)
matplotlib.rcParams.update({'xtick.major.size': 6})
matplotlib.rcParams.update({'ytick.major.size': 6})

# Légende (10)
matplotlib.rcParams.update({'legend.fontsize': 10})

# %% Setup des couleurs et légendes

# Définition des styles des simulations dans les graphiques (couleurs, forme de ligne taille...)
# Noms des couleurs : https://matplotlib.org/stable/gallery/color/named_colors.html
# Types de marqueurs : https://matplotlib.org/stable/api/markers_api.html
# Type de lignes : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
SimulationsLineStyleDictionary = {"H0Lat G-10Lat G0Sup": {"color": "red", "marker": "", "markersize": 1, "linestyle": "-", "linewidth": 1.5},
                                  "H0Lat G-10Lat G-6Sup": {"color": "green", "marker": "", "markersize": 1, "linestyle": "-", "linewidth": 1.5},
                                  "H0Lat G5Lat G0Sup": {"color": "blue", "marker": "", "markersize": 1, "linestyle": "-", "linewidth": 1.5},
                                  "H0Lat G5Lat G-6Sup": {"color": "black", "marker": "", "markersize": 1, "linestyle": "-", "linewidth": 1.5},

                                  "H15Lat G-10Lat G0Sup": {"color": "red", "marker": "", "markersize": 1, "linestyle": "--", "linewidth": 1.5},
                                  "H15Lat G-10Lat G-6Sup": {"color": "green", "marker": "", "markersize": 1, "linestyle": "--", "linewidth": 1.5},
                                  "H15Lat G5Lat G0Sup": {"color": "blue", "marker": "", "markersize": 1, "linestyle": "--", "linewidth": 1.5},
                                  "H15Lat G5Lat G-6Sup": {"color": "black", "marker": "", "markersize": 1, "linestyle": "--", "linewidth": 1.5},

                                  }

# Texte de description des simulations dans les légendes
SimulationDescriptionDictionary = {"H0Lat G-10Lat G0Sup": "Hum : 0 Lat ; Glen : -10 Lat, 0 Sup",
                                   "H0Lat G-10Lat G-6Sup": "Hum : 0 Lat ; Glen : -10 Lat, -6 Sup",
                                   "H0Lat G5Lat G0Sup": "Hum : 0 Lat ; Glen : 5 Lat, 0 Sup",
                                   "H0Lat G5Lat G-6Sup": "Hum : 0 Lat ; Glen : 5 Lat, -6 Sup",

                                   "H15Lat G-10Lat G0Sup": "Hum : 15 Lat ; Glen : -10 Lat, 0 Sup",
                                   "H15Lat G-10Lat G-6Sup": "Hum : 15 Lat ; Glen : -10 Lat, -6 Sup",
                                   "H15Lat G5Lat G0Sup": "Hum : 15 Lat ; Glen : 5 Lat, 0 Sup",
                                   "H15Lat G5Lat G-6Sup": "Hum : 15 Lat ; Glen : 5 Lat, -6 Sup",

                                   }

# Fonctions pour définir les légendes et styles des graphiques en fonction des noms des simulations dans les dictionnaires
define_simulations_line_style(SimulationsLineStyleDictionary)
define_simulation_description(SimulationDescriptionDictionary)

# %% Nom des simulations

MovementType_list = ["CoronalElevation", "ScapularElevation", "SagitalElevation"]

# glenoid_lateralisation_offset_list = [-10, -5, 0, 5]
# glenoid_superior_offset_list = [-6, -4, -2, 0]
# glenoid_lateral_offset = [0, 5, 10, 15]

glenoid_lateralisation_offset_list = [-10, 5]
glenoid_superior_offset_list = [-6, 0]
glenoid_lateral_offset_list = [0, 15]

# %%                                                Chargement des résultats sauvegardés
# Chemin d'accès au dossier dans lequel les fichiers ont été sauvegardés
SaveSimulationsDirectory = "Saved Simulations"

# Chargement des simulations
Results_Flexion = load_results_from_file(SaveSimulationsDirectory, "Results_Flexion")
Results_Abduction = load_results_from_file(SaveSimulationsDirectory, "Results_Abduction")
Results_Scapular = load_results_from_file(SaveSimulationsDirectory, "Results_Scapular")

Results = {"Coronal Elevation": Results_Abduction, "Scapular Elevation": Results_Scapular, "Sagital Elevation": Results_Flexion}

"""
GHReactions
"""
# Chargement des simulations
Results_Flexion_GHReactions = load_results_from_file(SaveSimulationsDirectory, "Results_Flexion_GHReactions")
Results_Abduction_GHReactions = load_results_from_file(SaveSimulationsDirectory, "Results_Abduction_GHReactions")
Results_Scapular_GHReactions = load_results_from_file(SaveSimulationsDirectory, "Results_Scapular_GHReactions")

Results_GHReactions = {"Coronal Elevation": Results_Abduction_GHReactions, "Scapular Elevation": Results_Scapular_GHReactions, "Sagital Elevation": Results_Flexion_GHReactions}

# %%                                                Chargement autres résultats et variables

# # Chargement des dictionnaires de variable
# SaveVariablesDirectory = "Saved VariablesDictionary"

# # Chargement des variables de simulation sauvegardées
# Variables = load_results_from_file(SaveVariablesDirectory, "Variables")

# %% Liste des catégories de muscles

# 9 muscles --> graphique 3x3
Muscles_Main = ["Deltoideus anterior",
                "Deltoideus lateral",
                "Deltoideus posterior",
                "Lower trapezius",
                "Middle trapezius",
                "Upper trapezius",
                "Rhomboideus",
                "Supraspinatus",
                "Serratus anterior"
                ]

# 9 muscles --> graphique 3x3
Muscles_Aux = ["Pectoralis major clavicular",
               "Pectoralis major sternal",
               "Pectoralis minor",
               "Subscapularis",
               "Teres major",
               "Teres minor",
               "Infraspinatus",
               "Biceps brachii long head",
               "Biceps brachii short head",
               ]

# 6 muscles --> graphique 2x3
Muscles_Extra = ["Sternocleidomastoid sternum",
                 "Sternocleidomastoid clavicular",
                 "Latissimus dorsi",
                 "Levator scapulae",
                 "Coracobrachialis",
                 "Triceps long head",
                 ]


# %% Graphiques

def rTSA_graphs(Results: dict, save_figures: bool = False):

    cases_hum_0Lat = ["H0Lat G-10Lat G-6Sup", "H0Lat G-10Lat G0Sup", "H0Lat G5Lat G-6Sup", "H0Lat G5Lat G0Sup"]
    cases_hum_15Lat = ["H15Lat G-10Lat G-6Sup", "H15Lat G-10Lat G0Sup", "H15Lat G5Lat G-6Sup", "H15Lat G5Lat G0Sup"]

    for movement in Results:
        current_result = Results[movement]

        # GH reaction force
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, composante_y=["AP"], subplot_title="anterior-posterior", subplot={"dimension": [1, 3], "number": 1})
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, composante_y=["IS"], subplot_title="inferior-superior", subplot={"dimension": [1, 3], "number": 2})
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, grid_x_step=20, composante_y=["ML"], subplot_title="medial-lateral", subplot={"dimension": [1, 3], "number": 3}, same_lim=True, hide_center_axis_labels=True, xlim=[0, 160])

        # GH reaction force
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, composante_y=["AP"], subplot_title="anterior-posterior", subplot={"dimension": [1, 3], "number": 1})
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, composante_y=["IS"], subplot_title="inferior-superior", subplot={"dimension": [1, 3], "number": 2})
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, grid_x_step=20, composante_y=["ML"], subplot_title="medial-lateral", subplot={"dimension": [1, 3], "number": 3}, same_lim=True, hide_center_axis_labels=True, xlim=[0, 160])

        # GH reaction force
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact", cases_on="all", composante_y=["AP"], subplot_title="anterior-posterior", subplot={"dimension": [1, 3], "number": 1})
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact", cases_on="all", composante_y=["IS"], subplot_title="inferior-superior", subplot={"dimension": [1, 3], "number": 2})
        graph(current_result, "Angle", "Reaction", f"{movement} : Force de contact", cases_on="all", grid_x_step=20, composante_y=["ML"], subplot_title="medial-lateral", subplot={"dimension": [1, 3], "number": 3}, same_lim=True, hide_center_axis_labels=True, xlim=[0, 160])

        # Instability ratio
        graph(current_result, "Angle", "Instability Ratio", f"{movement} : Instability ratio ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, grid_x_step=20, xlim=[0, 160], ylim=[0, 3])
        graph(current_result, "Angle", "Instability Ratio", f"{movement} : Instability ratio ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, grid_x_step=20, xlim=[0, 160], ylim=[0, 3])
        graph(current_result, "Angle", "Instability Ratio", f"{movement} : Instability ratio", cases_on="all", grid_x_step=20, xlim=[0, 160], ylim=[0, 3])

        # Fm Main
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Main, [3, 3], "Angle", "Fm", f"{movement} : Force musculaire ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160])
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Main, [3, 3], "Angle", "Fm", f"{movement} : Force musculaire ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160])
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Main, [3, 3], "Angle", "Fm", f"{movement} : Force musculaire", cases_on="all", hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160])

        # Fm aux
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Aux, [3, 3], "Angle", "Fm", f"{movement} : Force musculaire ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160])
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Aux, [3, 3], "Angle", "Fm", f"{movement} : Force musculaire ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160])
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Aux, [3, 3], "Angle", "Fm", f"{movement} : Force musculaire", cases_on="all", hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160])

        # Fm extra
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Extra, [2, 3], "Angle", "Fm", f"{movement} : Force musculaire ; 0mm latéralisation humérale", cases_on=cases_hum_0Lat, hide_center_axis_labels=True, same_lim=True, figsize=[18, 14], xlim=[0, 160])
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Extra, [2, 3], "Angle", "Fm", f"{movement} : Force musculaire ; 15mm latéralisation humérale", cases_on=cases_hum_15Lat, hide_center_axis_labels=True, same_lim=True, figsize=[18, 14], xlim=[0, 160])
        PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Extra, [2, 3], "Angle", "Fm", f"{movement} : Force musculaire", cases_on="all", hide_center_axis_labels=True, same_lim=True, figsize=[18, 14], xlim=[0, 160])

        # Sauvegarde des graphiques
        if save_figures:
            save_all_active_figures(save_folder_path="Graphiques", folder_name=f"{movement}", file_name=f"{movement}", save_format="png")


# Normal results
rTSA_graphs(Results, save_figures=True)

# %% Comparaison GHReactions


# for movement in Results:
#     Results_compare_GHReactions = {"GHReactions": Results_GHReactions[movement], "Joint Reaction": Results[movement]}
#     current_result = Results_compare_GHReactions

#     for case in Results_GHReactions[movement]:
#         PremadeGraphs.muscle_graph_from_list(current_result, Muscles_Main, [3, 3], "Angle", "Fm", f"{case} {movement} : Force musculaire", cases_on=[case], hide_center_axis_labels=True, same_lim=True, figsize=[24, 14], xlim=[0, 160], compare=True)

#         # Reaction force
#         graph(current_result, "Angle", "Reaction", f"{case} {movement} : Force de contact", cases_on=[case], composante_y=["AP"], subplot_title="anterior-posterior", subplot={"dimension": [1, 3], "number": 1}, compare=True)
#         graph(current_result, "Angle", "Reaction", f"{case} {movement} : Force de contact", cases_on=[case], composante_y=["IS"], subplot_title="inferior-superior", subplot={"dimension": [1, 3], "number": 2}, compare=True)
#         graph(current_result, "Angle", "Reaction", f"{case} {movement} : Force de contact", cases_on=[case], grid_x_step=20, composante_y=["ML"], subplot_title="medial-lateral", subplot={"dimension": [1, 3], "number": 3}, same_lim=True, hide_center_axis_labels=True, xlim=[0, 160], compare=True)


# %% Sauvegarde des résultats dans excel

# # Sauvegarde des résultats dans excel
# result_dictionary_to_excel(Results["Coronal Elevation"], "Coronal Elevation")
# result_dictionary_to_excel(Results["Scapular Elevation"], "Scapular Elevation")
# result_dictionary_to_excel(Results["Sagital Elevation"], "Sagital Elevation")
