from dashboard.models import OperationsModule
from utils.deltas import get_delta_percent, delta_to_color, get_delta_history
from utils.predict import operations_predict

import matplotlib.cm as cm 
import numpy as np
import json
from math import log

from module_templates import MODULES

N_MODULES = 9


# MODULES = [
#     {
#         'title': 'Profiles', 
#         'icon': '<i class="fas fa-users"></i>', 
#         'parts': [
#             'db_size_profiles_archive', 'db_size_profiles_frontend', 'db_size_individual'
#         ], 
#         'graphs': [
#             {   
#                 'type': 'doughnut', 
#                 'data': {
#                     'datasets': [
#                         {   'historical': False,
#                             'columns': ['db_size_profiles_archive', 'db_size_profiles_frontend', 'db_size_individual'], 
#                             'data': [],
#                             'backgroundColor': [delta_to_color(i, color_map=cm.gist_rainbow)[1] for i in (0, 0.5, 1.0)],                            
#                         }
#                     ],
#                     'dynamic_label': False,
#                     'labels': ['Archive', 'Frontend', 'Individual']
#                 },
#                 'options': {
#                     'title': {
#                         'display': 'true',
#                         'text': 'Profile Breakdown'
#                     }
#                 },
#             },
#             {                
#                 'type': 'line', 
#                 'data': {
#                     'datasets': [
#                         {   'historical': True,
#                             'columns': ['db_size_profiles_archive'], 
#                             'data': [],
#                             'label': 'Archive',
#                             'fill': 'false',
#                             'borderColor': delta_to_color(0, color_map=cm.gist_rainbow)[1],
#                             'backgroundColor': 'transparent',                            
#                         },
#                         {   'historical': True,
#                             'columns': ['db_size_profiles_frontend'],
#                             'data': [],
#                             'label': 'Frontend',
#                             'fill': 'false',
#                             'borderColor': delta_to_color(0.5, color_map=cm.gist_rainbow)[1],
#                             'backgroundColor': 'transparent',                            
#                         },
#                         {   'historical': True,
#                             'columns': ['db_size_individual'], 
#                             'data': [],
#                             'label': 'Individual',
#                             'fill': 'false',
#                             'borderColor': delta_to_color(1, color_map=cm.gist_rainbow)[1],
#                             'backgroundColor': 'transparent',                            
#                         }
#                     ],
#                     'dynamic_label': 'date',
#                     'labels': []
#                 },
#                 'options': {
#                     'title': {
#                         'display': 'true',
#                         'text': 'Historical Profile Increase'
#                     }
#                 }
#             }
#         ]
#     },
    
    
    
    
    
    
    # {'title': 'Locations', 'parts': ['db_size_location_raw'], 'icon': '<i class="fas fa-map-marker"></i>', 
    #     'data':{'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Emails', 'parts': ['db_size_emails'], 'icon': '<i class="fas fa-at"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Results', 'parts': ['db_size_search_engine'], 'icon': '<i class="fas fa-search"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Corporations', 'parts': ['db_size_corporations'], 'icon': '<i class="fas fa-building"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Technology', 'parts': ['db_size_technology'], 'icon': '<i class="fas fa-space-shuttle"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Websites', 'parts': ['db_size_websites_processed'], 'icon': '<i class="fas fa-globe"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Appended', 'parts': ['db_size_appended'], 'icon': '<i class="fas fa-user-plus"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
    #     'graphs': []},
    # {'title': 'Campaigns', 'parts': ['db_size_email_campaign'], 'icon': '<i class="fas fa-envelope"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        # 'graphs': []}
# ]


def generate_modules(): 
    current_record = OperationsModule.objects.last()
    modules = []

    i = 0
    for module in MODULES:
        # background = cm.gist_rainbow
        # if (i++ %% 2 == 0) background = cm.brg

        title = module['title']
        parts = [getattr(current_record, part) for part in module['parts']]

        current_total = sum(parts)
        last_total = sum([getattr(OperationsModule.objects.get(pk=current_record.pk - 1), part) for part in module['parts']])

        history = [sum([getattr(record, part) for part in module['parts']]) for record in OperationsModule.objects.all()]
        next_total = operations_predict(history)
        delta_value, delta_color = delta_to_color(get_delta_percent(history))

        for graph in module['graphs']:
            dynamic_label = graph['data']['dynamic_label']
            
            datasets = graph['data']['datasets']
            
            for dataset in datasets: 
                if dataset['historical']: 
                    dataset['data'] = [getattr(record, part) - getattr(OperationsModule.objects.first(), part) for part in dataset['columns'] for record in OperationsModule.objects.all()]
                elif title == 'Locations': 
                    dataset['data'] = [getattr(current_record, 'db_size_location_raw') - getattr(current_record, 'db_size_location_parsed'), getattr(current_record, 'db_size_location_parsed')]
                else:
                    dataset['data'] = [getattr(current_record, part) for part in dataset['columns']]    

            if dynamic_label: 
                graph['data']['labels'] = [str(getattr(record, dynamic_label)) for record in OperationsModule.objects.all()]

            # if 
                

        modules.append(
            {
                'title': title, 
                'last': "{:,}".format(last_total),
                'current': "{:,}".format(current_total),
                'next': "{:,}".format(next_total),
                'delta_value': int(delta_value*100),
                'delta_color': delta_color,                
                'icon': module['icon'], 
                'graphs': json.dumps(module['graphs'])
            }
        )
    return modules






# {
#     type: chart_type,
#     data: {
#         datasets: [{
#         data: values,
#         backgroundColor: colors,
#         }],
#         labels: labels
#     },
# }

