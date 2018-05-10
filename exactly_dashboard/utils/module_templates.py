from deltas import get_delta_percent, delta_to_color, get_delta_history

import matplotlib.cm as cm 


BRG = cm.brg
GR = cm.gist_rainbow

PROFILES_MODULE = {
        'title': 'Profiles', 
        'icon': '<i class="fas fa-users"></i>', 
        'parts': [
            'db_size_profiles_archive', 'db_size_profiles_frontend', 'db_size_individual'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_profiles_archive', 'db_size_profiles_frontend', 'db_size_individual'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=GR)[1] for i in (0, 0.5, 1.0)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Archive', 'Frontend', 'Individual']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Profile Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_profiles_archive'], 
                            'data': [],
                            'label': 'Archive',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        },
                        {   'historical': True,
                            'columns': ['db_size_profiles_frontend'],
                            'data': [],
                            'label': 'Frontend',
                            'fill': 'false',
                            'borderColor': delta_to_color(0.5, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        },
                        {   'historical': True,
                            'columns': ['db_size_individual'], 
                            'data': [],
                            'label': 'Individual',
                            'fill': 'false',
                            'borderColor': delta_to_color(1, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Profile Increase'
                    }
                }
            }
        ]
    }
    
LOCATIONS_MODULE = {
        'title': 'Locations', 
        'icon': '<i class="fas fa-map-marker"></i>', 
        'parts': [
            'db_size_location_raw'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_location_raw', 'db_size_location_parsed'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=BRG)[1] for i in (0, 1)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Unparsed', 'Parsed']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Locations Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_location_raw'], 
                            'data': [],
                            'label': 'Raw',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=BRG)[1],
                            'backgroundColor': 'transparent',                            
                        },
                        {   'historical': True,
                            'columns': ['db_size_location_parsed'],
                            'data': [],
                            'label': 'Parsed',
                            'fill': 'false',
                            'borderColor': delta_to_color(1, color_map=BRG)[1],
                            'backgroundColor': 'transparent',                            
                        },
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Locations Increase'
                    }
                }
            }
        ]
    }

EMAILS_MODULE = {
        'title': 'Email', 
        'icon': '<i class="fas fa-at"></i>', 
        'parts': [
            'db_size_emails'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_emails'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=GR)[1] for i in (0,)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Emails']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Emails Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_emails'], 
                            'data': [],
                            'label': 'Emails',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Emails Increase'
                    }
                }
            }
        ]
    }

SE_MODULE = {
        'title': 'Results', 
        'icon': '<i class="fas fa-search"></i>', 
        'parts': [
            'db_size_search_engine'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_search_engine'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=BRG)[1] for i in (0,)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Results']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Results Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_search_engine'], 
                            'data': [],
                            'label': 'Results',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=BRG)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Results Increase'
                    }
                }
            }
        ]
    }

CORPORATIONS_MODULE = {
        'title': 'Corporations', 
        'icon': '<i class="fas fa-building"></i>', 
        'parts': [
            'db_size_corporations'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_corporations'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=GR)[1] for i in (0,)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Corporations']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Corporations Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_corporations'], 
                            'data': [],
                            'label': 'Corporations',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Corporations Increase'
                    }
                }
            }
        ]
    }

TECH_MODULE = {
        'title': 'Technology', 
        'icon': '<i class="fas fa-space-shuttle"></i>', 
        'parts': [
            'db_size_technology'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_technology'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=BRG)[1] for i in (0,)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Technology']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Technology Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_technology'], 
                            'data': [],
                            'label': 'Technology',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=BRG)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Technology Increase'
                    }
                }
            }
        ]
    }

WEBSITES_MODULE = {
        'title': 'Websites', 
        'icon': '<i class="fas fa-globe"></i>', 
        'parts': [
            'db_size_websites_processed'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_websites_processed'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=GR)[1] for i in (0,)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Websites']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Websites Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_websites_processed'], 
                            'data': [],
                            'label': 'Websites',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Websites Increase'
                    }
                }
            }
        ]
    }

APPENDED_MODULE = {
        'title': 'Appended', 
        'icon': '<i class="fas fa-user-plus"></i>', 
        'parts': [
            'db_size_appended'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_appended'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=BRG)[1] for i in (0,)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Appended']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Appended Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_appended'], 
                            'data': [],
                            'label': 'Appended',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=BRG)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Appended Increase'
                    }
                }
            }
        ]
    }

CAMPAIGN_MODULE = {
        'title': 'Campaigns', 
        'icon': '<i class="fas fa-envelope"></i>', 
        'parts': [
            'db_size_email_campaign'
        ], 
        'graphs': [
            {   
                'type': 'doughnut', 
                'data': {
                    'datasets': [
                        {   'historical': False,
                            'columns': ['db_size_email_campaign_marketing', 'db_size_email_campaign_csuite'], 
                            'data': [],
                            'backgroundColor': [delta_to_color(i, color_map=GR)[1] for i in (0, 1.0)],                            
                        }
                    ],
                    'dynamic_label': False,
                    'labels': ['Marketing Professionals', 'Executives']
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Email Campaign List Breakdown'
                    }
                },
            },
            {                
                'type': 'line', 
                'data': {
                    'datasets': [
                        {   'historical': True,
                            'columns': ['db_size_email_campaign'], 
                            'data': [],
                            'label': 'Email Campaign List Size',
                            'fill': 'false',
                            'borderColor': delta_to_color(0, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        },
                        {   'historical': True,
                            'columns': ['db_size_email_campaign_marketing'],
                            'data': [],
                            'label': 'Marketing Professionals',
                            'fill': 'false',
                            'borderColor': delta_to_color(0.5, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        },
                        {   'historical': True,
                            'columns': ['db_size_email_campaign_csuite'], 
                            'data': [],
                            'label': 'Executives',
                            'fill': 'false',
                            'borderColor': delta_to_color(1, color_map=GR)[1],
                            'backgroundColor': 'transparent',                            
                        }
                    ],
                    'dynamic_label': 'date',
                    'labels': []
                },
                'options': {
                    'title': {
                        'display': 'true',
                        'text': 'Historical Email Campaign List Size Increase'
                    }
                }
            }
        ]
    }


MODULES = [PROFILES_MODULE, LOCATIONS_MODULE, EMAILS_MODULE, SE_MODULE, CORPORATIONS_MODULE, TECH_MODULE, WEBSITES_MODULE, APPENDED_MODULE, CAMPAIGN_MODULE]
    
    # {'title': 'Campaigns', 'parts': ['db_size_email_campaign'], 'icon': '<i class="fas fa-envelope"></i>', 
    #     'data': {'chart_type': 'line', 'labels': '', 'colors': ''}, 
        # 'graphs': []}
