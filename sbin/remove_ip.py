#!/usr/bin/python3

import sys

hosts_file = open(sys.argv[1])
hosts_file_list = hosts_file.read().split('\n')
hosts_file.close()

targets = []
for target in sys.argv[2:]:
    target_rule = 'ALL: %s' % (target,)
    if target_rule in hosts_file_list:
        hosts_file_list.remove(target_rule)

hosts_file = open(sys.argv[1], 'w')
hosts_file.write('\n'.join(hosts_file_list))
hosts_file.close()

# TODO allow removal.
