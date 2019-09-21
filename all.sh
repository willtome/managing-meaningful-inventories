#!/bin/bash
./sqlite_setup.sh
export ANSIBLE_NOCOWS=1
echo "GCP Compute inventory plugin scenario"
echo "  will not print output (too big), but count lines in output"
ansible-inventory -i 01_gcp/private.gcp_compute.yml --list --export | wc -l
echo "Azure RM inventory plugin scenario"
./02_azure/set_env.sh
ansible-playbook -i 02_azure/azure_rm.yaml debug.yml
echo "SQlite3 custom inventory plugin scenario"
ansible-inventory -i 03_sqlite/sqlite.yml --playbook-dir=03_sqlite --list --export
echo "SQLite3 inventory script scenario"
# this does not need --playbook-dir, because no plugin
SQLITE_DATABASE_PATH=hosts.db SQLITE_DATABASE_TABLE=hosts ansible-inventory -i 04_as_script/sqlite_script.py --list --export
echo "Basic example"
# got fancy with the bash script here
./05_basic/run.sh
