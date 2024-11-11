import pandas as pd
import datetime
import random
# 1: monday, 7: sunday
start_date = '7/1/2021'
start_day = 4
end_date = '6/30/2022'
date_format = '%m/%d/%Y'
end_day = 4
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def compute_day_week(date: datetime.datetime):
    return date.weekday() + 1

"""
Return list [{weeks: str, hrs: number}]
"""
def compute_business_weeks(start_date, end_date):
    result = []
    start = datetime.datetime.strptime(start_date, date_format)
    end = datetime.datetime.strptime(end_date, date_format)
    total_days = (end-start).days
    week_start_date = start
    week_end_date = None
    
    for i in range(1, total_days + 1):
        date_obj = start + datetime.timedelta(i)
        if compute_day_week(date_obj) == 5:
            week_end_date = date_obj
            result.append({
                'week': f"{week_start_date.strftime(date_format)} - {week_end_date.strftime(date_format)}",
                'days': (week_end_date - week_start_date).days + 1,
            })
        
        if compute_day_week(date_obj) == 1:
            week_start_date = date_obj
            
    return result


# generate random_results
def generate_random_results(result, seed: int, lowest_hr, highest_hr, average_hr):
    random.seed(seed)
    for i, week_dict in enumerate(result):
        days = week_dict['days']
        hrs = random.randint(lowest_hr, highest_hr)
        result[i]['hrs'] = hrs * days + days * average_hr
    
    return result
        
result = compute_business_weeks(start_date, end_date)
result_hrs = generate_random_results(result, 6, 0, 3, 8)

result_hrs_pd = pd.DataFrame(result_hrs)
print(result_hrs_pd, '===')
result_hrs_pd.to_excel('work_hours.xlsx', index=False)