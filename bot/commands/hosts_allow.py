import subprocess
from ipaddress import IPv4Address

from ..app import slack

@slack.command('etc/hosts.allow', token='DY5Qkf3BHaukpKWOBxsfjpB2',
        team_id='T3QDD12QK', methods=['POST'])
def allow(**kwargs):
    target = kwargs.get('text')

    try:
        IPv4Address(target)
    except ValueError:
        return  slack.response(target + ' is not IPv4', response_type='in_channel')

    add_py = subprocess.Popen(('/usr/bin/sudo sbin/add_ip.py %s %s'
        % ('/etc/hosts.allow', target)).split(), shell=False)
    add_py.wait(timeout=10)

    remove_py = subprocess.Popen(('/usr/bin/sudo sbin/remove_ip.py %s %s'
        % ('/etc/hosts.deny', target)).split(), shell=False)
    remove_py.wait(timeout=10)
    return slack.response(target + ' unbanned', response_type='in_channel')

