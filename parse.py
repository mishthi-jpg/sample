import json
from datetime import datetime, timezone
import re

log_path = 'access.log'

count_200 = 0
count_500 = 0
total_lines = 0

with open(log_path, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total_lines += 1
        if '200' in line:
            count_200 += 1
        elif '500' in line:
            count_500 += 1

summary = {
    "source_file": log_path,
    "total_lines_processed": total_lines,
    "status_200": count_200,
    "status_500": count_500,
    "generated_at": datetime.now(timezone.utc).isoformat()
}


with open('log_summary.json', 'w') as json_file:
    json.dump(summary, json_file, indent=2)

print(f"Log summary written to log_summary.json")
print(summary)


#REgex parsing of log file


four_hundred_count = 0
five_hundred_count = 0
 
with open("access_errors.log", "r") as l:
    log_data = l.read()
    for lines in l:
        lines=lines.strip() 
        if not lines:
            continue
        if '400' in lines:
            print("yep 400")
            four_hundred_count = four_hundred_count + 1
        elif '500' in lines:
            print("yep 500")
            five_hundred_count = five_hundred_count + 1

pattern = r'"\s*([1-5]\d{2})\s'

status_codes = re.findall(pattern, log_data)
print(status_codes)
print(f"Count of 400 status codes: {four_hundred_count}")
print(f"Count of 500 status codes: {five_hundred_count}")