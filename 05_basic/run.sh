#!/bin/bash
SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
ansible-inventory -i $SCRIPT_DIR/basic.yml --list --export --playbook-dir=$SCRIPT_DIR
