from dashboard.models import OperationsModule
from utils.deltas import get_delta_percent, delta_to_color
from utils.predict import operations_predict
from module_templates import MODULES

import json

N_MODULES = 9


def generate_modules(): 
    current_record = OperationsModule.objects.last()
    modules = []

    for module in MODULES:
        title = module['title']
        parts = module['columns']

        history = [sum([getattr(record, part) for part in parts]) for record in OperationsModule.objects.all()]


        last_total = sum([getattr(OperationsModule.objects.get(pk=current_record.pk - 1), part) for part in parts])
        current_total = sum([getattr(current_record, part)  for part in parts])
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
