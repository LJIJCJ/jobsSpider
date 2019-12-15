import sqlite3

conn = sqlite3.connect('../jobs')
c = conn.cursor()

cursor = c.execute('SELECT * FROM jobs')
for raw in cursor:
    print('position_id=%s,position_name=%s,position_lables=%s,work_year=%s,salary=%s,city=%s,education=%s,company_name=%s,industry_field=%s,finance_stage=%s,company_size=%s,updated_at=%s,time=%s,platform=%s,avg_salary=%s'%raw[1:])
    print('')

conn.close()