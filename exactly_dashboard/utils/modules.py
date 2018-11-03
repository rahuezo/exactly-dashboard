from dashboard.models import OperationsModule
from utils.deltas import get_delta_percent, delta_to_color
from utils.predict import operations_predict
# from operations_modules_templates import MODULES
from utils.operations_modules_templates import DB_STATS_MODULE_TEMPLATES

import json

N_MODULES = 9

# def modules_to_records(modules): 
#     records = []

#     for module in modules: 
#         record = {}

#         if 



# date = models.DateField()
# db_size_profiles_archive = models.IntegerField(default=0)
# db_size_profiles_frontend = models.IntegerField(default=0)
# db_size_individual = models.IntegerField(default=0)
# db_size_location_raw = models.IntegerField(default=0)
# db_size_location_parsed = models.IntegerField(default=0)
# db_size_emails = models.IntegerField(default=0)
# db_size_search_engine = models.IntegerField(default=0)
# db_size_corporations = models.IntegerField(default=0)
# db_size_technology = models.IntegerField(default=0)
# db_size_websites_processed = models.IntegerField(default=0)
# db_size_appended = models.IntegerField(default=0)
# db_size_email_campaign = models.IntegerField(default=0)
# db_size_email_campaign_marketing = models.IntegerField(default=0)
# db_size_email_campaign_csuite = models.IntegerField(default=0)






def generate_modules(modules_list): 

    current_record = {}
    
    for module in modules_list: 
        current_record[module.name] = module.records[-1]



    # current_record = OperationsModule.objects.last()

    modules = []

    for module_template in DB_STATS_MODULE_TEMPLATES:
        title = module_template['title']
        parts = module_template['columns']

        group = filter(lambda x: x.name in parts, modules_list)

        group_history = [[member.records[i][1] for member in group] for i in xrange(len(group[0].records))]

        history = map(sum, group_history)



        # history = [sum([getattr(record, part) for part in parts]) for record in OperationsModule.objects.all()]

        last_total = sum([member.records[-2][1] for member in group])

        # last_total = sum([getattr(OperationsModule.objects.get(pk=current_record.pk - 1), part) for part in parts])


        current_total = sum([member.records[-1][1]  for member in group])

        # current_total = sum([getattr(current_record, part)  for part in parts])
        next_total = operations_predict(history)

        delta_value, delta_color = delta_to_color(get_delta_percent(history))

        for graph in module_template['graphs']:
            dynamic_label = graph['data']['dynamic_label']
            
            datasets = graph['data']['datasets']
            
            for dataset in datasets: 
                if dataset['historical']: 

                    dataset['data'] = group_history
                    
                    # dataset['data'] = [getattr(record, part) - getattr(OperationsModule.objects.first(), part) for part in dataset['columns'] for record in OperationsModule.objects.all()]
                elif title == 'Locations': 
                    dataset['data'] = [current_record['db_size_location_raw'][1] - current_record['db_size_location_parsed'][1], current_record['db_size_location_parsed'][1]]
                    # dataset['data'] = [getattr(current_record, 'db_size_location_raw') - getattr(current_record, 'db_size_location_parsed'), getattr(current_record, 'db_size_location_parsed')]
                else:
                    dataset['data'] = [current_record[part][1] for part in parts]    

            if dynamic_label: 
                graph['data']['labels'] = [str(record[0]) for record in modules_list[0].records]

                # graph['data']['labels'] = [str(getattr(record, dynamic_label)) for record in OperationsModule.objects.all()]

        modules.append(
            {
                'title': title, 
                'last': "{:,}".format(last_total),
                'current': "{:,}".format(current_total),
                'next': "{:,}".format(next_total),
                'delta_value': int(delta_value*100),
                'delta_color': delta_color,                
                'icon': module_template['icon'], 
                'graphs': json.dumps(module_template['graphs'])
            }
        )
    return modules

# modules = []

# for module in modules_list:
#     title = module['title']
#     parts = module['columns']

#     history = [sum([getattr(record, part) for part in parts]) for record in OperationsModule.objects.all()]


#     last_total = sum([getattr(OperationsModule.objects.get(pk=current_record.pk - 1), part) for part in parts])
#     current_total = sum([getattr(current_record, part)  for part in parts])
#     next_total = operations_predict(history)

#     delta_value, delta_color = delta_to_color(get_delta_percent(history))

#     for graph in module['graphs']:
#         dynamic_label = graph['data']['dynamic_label']
        
#         datasets = graph['data']['datasets']
        
#         for dataset in datasets: 
#             if dataset['historical']: 
#                 dataset['data'] = [getattr(record, part) - getattr(OperationsModule.objects.first(), part) for part in dataset['columns'] for record in OperationsModule.objects.all()]
#             elif title == 'Locations': 
#                 dataset['data'] = [getattr(current_record, 'db_size_location_raw') - getattr(current_record, 'db_size_location_parsed'), getattr(current_record, 'db_size_location_parsed')]
#             else:
#                 dataset['data'] = [getattr(current_record, part) for part in dataset['columns']]    

#         if dynamic_label: 
#             graph['data']['labels'] = [str(getattr(record, dynamic_label)) for record in OperationsModule.objects.all()]

#     modules.append(
#         {
#             'title': title, 
#             'last': "{:,}".format(last_total),
#             'current': "{:,}".format(current_total),
#             'next': "{:,}".format(next_total),
#             'delta_value': int(delta_value*100),
#             'delta_color': delta_color,                
#             'icon': module['icon'], 
#             'graphs': json.dumps(module['graphs'])
#         }
#     )
# return modules
