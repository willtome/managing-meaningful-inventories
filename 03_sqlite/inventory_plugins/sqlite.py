DOCUMENTATION = '''
    name: SQLite Inventory
    plugin_type: inventory
    author:
      - Will Tome (@willtome)
      - Alan Rominger (@AlanCoding)
    short_description: Dynamic inventory plugin for a SQLite database.
    version_added: "n/a"
    inventory: sqlite
    options:
        plugin:
            description: Token that ensures this is a source file for the plugin.
            required: True
            choices: ['sqlite']
        db_path:
            description:
                - The path to the sqlite db file.
                - This can be either an absolute path, or relative to inventory file.
            required: True
        db_table:
            description: The table containing hosts
            required: True
    requirements:
        - python >= 2.7
        - sqlite >= 3.0
'''
EXAMPLES = r'''
# example sqlite.yml file
---
plugin: sqlite
db_path: hosts.db
db_table: hosts
'''

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseFileInventoryPlugin

import sqlite3

import os


class InventoryModule(BaseFileInventoryPlugin):

    NAME = 'sqlite'

    def verify_file(self, path):
      super(InventoryModule, self).verify_file(path)
      return path.endswith(('sqlite.yml', 'sqlite.yaml'))

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)

        db_file_in = self.get_option('db_path')
        if os.path.isabs(db_file_in):
            db_file = db_file_in
        else:
            db_file = os.path.join(os.path.dirname(path), db_file_in)
        db_table = self.get_option('db_table')
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM {tn}" .format(tn=db_table))
        # Add each host in table
        for row in c.fetchall():
            # Split comma separated list of group names from DB
            for group in row[3].split(','):
                # Add group to inventory and host to group
                group_name = self.inventory.add_group(group)
                host_name = self.inventory.add_host(row[1],group_name)
            # Set variables for each host
            self.inventory.set_variable(host_name,'ansible_host', row[2])
            self.inventory.set_variable(host_name,'db_id', row[0])
