#!/bin/bash
rm 03_sqlite/hosts.db
sqlite3 03_sqlite/hosts.db <<EOF
CREATE TABLE hosts(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  name TEXT NOT NULL, ip TEXT NOT NULL, groups TEXT NOT NULL);
INSERT INTO hosts(name, ip, groups) VALUES ('web1', '192.168.1.21','web,primary');
INSERT INTO hosts(name, ip, groups) VALUES ('web2', '192.168.1.22','web,secondary');
EOF