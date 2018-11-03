from utils.deltas import get_delta_percent, delta_to_color
from datetime import datetime


class Module:
    def __init__(self, fields={}): 
        self.fields = fields

    def add(self, key, val):
        self.fields[key] = val.lower()

    def get(self, key): 
        if key in self.fields: 
            return self.fields[key]
        return None



class LeadsCard: 
    def __init__(self, module): 
        self.module = module
        self.steps = ["p", "f", "b", "complete"]
        self.project_name = module.fields.get("name")
        self.client_website = module.fields.get("client website")
        self.client_contact = module.fields.get("client contact")
        self.client_location = module.fields.get("client location")
        
        self.project_type = module.fields.get("project type")
        self.project_lead = module.fields.get("project lead")
        self.asana_link = module.fields.get("asana link")
        self.status = module.fields.get("status")
        self.estimated_completion = module.fields.get("estimated completion")
        self.start_date = module.fields.get("start date")
        self.end_date = module.fields.get("end date")

        self.required_companies = module.fields.get("required companies")
        self.required_leads = module.fields.get("required leads")
        self.required_leads_company = module.fields.get("required leads/company")
        self.required_geography = module.fields.get("required geography")
        self.required_industries = module.fields.get("required industries")
        self.required_technologies = module.fields.get("required technologies")
        self.required_company_size = module.fields.get("required company size")
        self.required_revenue = module.fields.get("required revenue")
        self.required_leads_location = module.fields.get("required leads/location")
        self.required_titles = module.fields.get("required titles")

        self.outline_human_time = module.fields.get("outline human time")

        self.review_human_time = module.fields.get("review human time")

        self.company_gather_human_time = module.fields.get("company gather human time")
        self.company_gather_elapsed_time = module.fields.get("company gather elapsed time")
        self.company_gather_company_count = module.fields.get("company gather company count")

        self.profile_gather_human_time = module.fields.get("profile gather human time")
        self.profile_gather_elapsed_time = module.fields.get("profile gather elapsed time")
        self.profile_gather_company_count = module.fields.get("profile gather company count")
        self.profile_gather_individual_count = module.fields.get("profile gather individual count")

        self.validation_human_time = module.fields.get("validation human time")
        self.validation_elapsed_time = module.fields.get("validation elapsed time")
        self.validation_company_count = module.fields.get("validation company count")
        self.validation_individual_count = module.fields.get("validation individual count")

        self.qc_human_time = module.fields.get("qc human time")
        self.qc_elapsed_time = module.fields.get("qc elapsed time")
        self.qc_company_count = module.fields.get("qc company count")
        self.qc_individual_count = module.fields.get("qc individual count")
        
        self.time_human = sum(map(lambda x: 0 if len(x.strip()) == 0 else int(x), [self.outline_human_time, self.review_human_time, self.company_gather_human_time, self.profile_gather_human_time, self.validation_human_time, self.qc_human_time]))
        self.time_elapsed = sum(map(lambda x: 0 if len(x.strip()) == 0 else int(x),[self.company_gather_elapsed_time, self.profile_gather_elapsed_time, self.validation_elapsed_time, self.qc_elapsed_time]))
           
        for count in ["0", self.company_gather_company_count, self.profile_gather_company_count, self.validation_company_count, self.qc_company_count]:
            if len(count.strip()) == 0:
                break       
            self.current_companies = int(count)
            self.current_companies_color = delta_to_color(self.current_companies / float(self.required_companies), "lead", raw=True, scale_shift=0)

        for count in ["0", self.profile_gather_individual_count, self.validation_individual_count, self.qc_individual_count]:
            if len(count.strip()) == 0:
                break       
            self.current_individuals = int(count)
            self.current_individuals_color = delta_to_color(self.current_individuals / float(self.required_leads), "lead", raw=True, scale_shift=0)


        self.status_percent = ((self.steps.index(self.status.lower()) + 1) / float(len(self.steps)))*100 if len(self.status.strip()) > 0 else 0


class DbCard:
    def __init__(self, module): 
        self.name = None
        self.records = []

        for field in module.fields: 
            if field == "name": 
                self.name = module.fields.get(field)
            else: 
                date = datetime.strptime(field, "%m/%d/%Y")
                self.records.append((date, int(module.fields.get(field).replace(',', ''))))

        self.records.sort(key=lambda x: x[0])

    def __str__(self): 
        return self.name





# class ReportsCard: 
#     def __init__(self, module): 
#         self.module = module

# class UpworkCard: 
#     def __init__(self, module): 
#         self.module = module



        