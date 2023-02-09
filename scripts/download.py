import canvas
import os, os.path
import json
import csv
import sys

asst_name = 'HW3'

asst_id = canvas.asst_byname(asst_name)
users = {user_id:netid for (netid, user_id) in canvas.users_bynetid().items()}

writer = csv.writer(sys.stdout)

for record in canvas.list_subs(asst_id):
    for sub in record['submission_history']:
        if sub['attempt'] is not None:
            netid = users[sub['user_id']]
            attempt = sub['attempt']
            writer.writerow((netid, attempt, sub["submitted_at"]))
            dir = os.path.join(asst_name, netid, f'attempt_{attempt}')
            os.makedirs(dir, exist_ok=True)
            for att in sub['attachments']:
                canvas.download(att['url'], os.path.join(dir, att['filename']))
