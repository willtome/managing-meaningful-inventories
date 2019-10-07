### Basic Inventory Plugin

This is a demo inventory plugin, packaged as part of a collection.

How to package, from this folder:

```
ansible-galaxy collection build
```

You can upload this in the Ansible Galaxy UI!
(you may have to replace instances of "alancoding" with your username)

If you actually use this, it will take the input `count` and make that
many hosts.

You can then install the content either from the `.tar.gz` file
or from the output of the build command. After you have done that
you can test with:

```
ansible-inventory -i example.basic.yml --list --export --playbook-dir=.
```

(if ran from this directory)
