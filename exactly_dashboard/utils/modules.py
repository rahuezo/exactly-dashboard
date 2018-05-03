from dashboard.models import OperationsModule
from utils.deltas import get_delta_percent, delta_to_color
from utils.predict import operations_predict

N_MODULES = 9
MODULES = [
    {'title': 'Profiles', 'parts': [
        'db_size_profiles_archive', 'db_size_profiles_frontend', 'db_size_individual' 
        ], 'icon': '<i class="fas fa-users"></i>', 'data':{'chart_type': 'pie', 'labels': ['Archive', 'Frontend', 'Individual'], 'colors': ''}, 
        'graphs': [{'chart_type': 'line', 'data_column': 'db_size_profiles_archive', 'labels':''}]},
    {'title': 'Locations', 'parts': ['db_size_location_raw'], 'icon': '<i class="fas fa-map-marker"></i>', 
        'data':{'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Emails', 'parts': ['db_size_emails'], 'icon': '<i class="fas fa-at"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Results', 'parts': ['db_size_search_engine'], 'icon': '<i class="fas fa-search"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Corporations', 'parts': ['db_size_corporations'], 'icon': '<i class="fas fa-building"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Technology', 'parts': ['db_size_technology'], 'icon': '<i class="fas fa-space-shuttle"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Websites', 'parts': ['db_size_websites_processed'], 'icon': '<i class="fas fa-globe"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Appended', 'parts': ['db_size_appended'], 'icon': '<i class="fas fa-user-plus"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []},
    {'title': 'Campaigns', 'parts': ['db_size_email_campaign'], 'icon': '<i class="fas fa-envelope"></i>', 
        'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        'graphs': []}
]


def generate_modules(): 
    current_record = OperationsModule.objects.last()
    modules = []

    for module in MODULES:
        title = module['title']
        parts = [getattr(current_record, part) for part in module['parts']]

        current_total = sum(parts)
        last_total = sum([getattr(OperationsModule.objects.get(pk=current_record.pk - 1), part) for part in module['parts']])

        history = [sum([getattr(record, part) for part in module['parts']]) for record in OperationsModule.objects.all()]
        next_total = operations_predict(history)
        delta_value, delta_color = delta_to_color(get_delta_percent(history))

        modules.append(
            {
                'title': title, 
                'last': "{:,}".format(last_total),
                'current': "{:,}".format(current_total),
                'next': "{:,}".format(next_total),
                'delta_value': int(delta_value*100),
                'delta_color': delta_color,                
                'icon': module['icon'], 
                'values': parts,
                'chart_type': module['data']['chart_type'],
                'labels': module['data']['labels'],
                'colors': ['#F15854', '#60BD68', '#5DA5DA'], # module['data']['colors']                
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

