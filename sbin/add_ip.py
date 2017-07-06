#!/usr/bin/python3

import sys

hosts_file = open(sys.argv[1])
hosts_file_list = hosts_file.read().split('\n')
hosts_file.close()

if not hosts_file_list[-1]:  # FIXME: WTF moment
    hosts_file_list.pop()

targets = []
for target in sys.argv[2:]:
    target_rule = 'ALL: %s' % (target,)
    if target_rule not in hosts_file_list:
        targets.append(target_rule)

hosts_file_list.extend(targets)
hosts_file_list.append('')  # XXX: SSH BLOCKER: need to add new line at the end.

hosts_file = open(sys.argv[1], 'w')
hosts_file.write('\n'.join(hosts_file_list))
hosts_file.close()

# TODO allow removal.
