#!/usr/bin/python3

import sys

hosts_deny = open('/etc/hosts.deny')
hosts_deny_list = hosts_deny.read().split('\n')
hosts_deny.close()

if not hosts_deny_list[-1]:  # FIXME: WTF moment
    hosts_deny_list.pop()

targets = []
for target in sys.argv[1:]:
    target_rule = 'ALL: %s' % (target,)
    if target_rule not in hosts_deny_list:
        targets.append(target_rule)

hosts_deny_list.extend(targets)

hosts_deny = open('/etc/hosts.deny', 'w')
hosts_deny.write('\n'.join(hosts_deny_list))
hosts_deny.close()

# TODO allow removal.
