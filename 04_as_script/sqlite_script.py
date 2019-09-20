#!/usr/bin/env python

# How to use: set environment variables for input
# SQLITE_DATABASE_PATH=hosts.db
# SQLITE_DATABASE_TABLE=hosts

import sqlite3
import os
import json


r = {
    '_meta': {
        'hostvars': {}
    }
}


db_file_in = os.environ.get('SQLITE_DATABASE_PATH')

if os.path.isabs(db_file_in):
    db_file = db_file_in
else:
    db_file = os.path.join(os.path.dirname(__file__), db_file_in)

db_table = os.environ.get('SQLITE_DATABASE_TABLE')

conn = sqlite3.connect(db_file)
c = conn.cursor()
c.execute("SELECT * FROM {tn}" .format(tn=db_table))

# Add each host in table
for row in c.fetchall():
    # Split comma separated list of group names from DB
    host = row[1]
    r['_meta']['hostvars'][host] = {}
    for group in row[3].split(','):
        # Add group to inventory and host to group
        if group in r:
            r[group]['hosts'].append(host)
        else:
            r[group] = {'hosts': [host]}
    # Set variables for each host
    r['_meta']['hostvars'][host]['ansible_host'] = row[2]
    r['_meta']['hostvars'][host]['db_id'] = row[0]

print(json.dumps(r, indent=2))
