SQLITE_DATABASE_PATH=hosts.db SQLITE_DATABASE_TABLE=hosts ansible-inventory -i sqlite_script.py --list --export
