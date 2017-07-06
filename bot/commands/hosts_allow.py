import subprocess

from ..app import slack

@slack.command('etc/hosts.allow', token='',
        team_id='T3QDD12QK', methods=['POST'])
def allow(**kwargs):
    target = kwargs.get('text')
    add_py = subprocess.Popen(('/usr/bin/sudo sbin/hosts_deny.py %s %s'
        % ('/etc/hosts.allow', target)).split(), shell=False)
    add_py.wait(timeout=10)

    remove_py = subprocess.Popen(('/usr/bin/sudo sbin/remove_ip.py %s %s'
        % ('/etc/hosts.deny', target)).split(), shell=False)
    remove_py.wait(timeout=10)
    return slack.response(target + ' banned', response_type='in_channel')
