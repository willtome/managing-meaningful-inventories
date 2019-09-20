echo "Correct use of ansible-inventory"
ansible-inventory -i sqlite.yml --list --export --playbook-dir=.
echo "Correct use of ansible-doc"
ANSIBLE_INVENTORY_PLUGINS=. ansible-doc -t inventory -l