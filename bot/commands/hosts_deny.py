import subprocess

from ..app import slack


@slack.command('etc/hosts.deny', token='zHBMFbpek0MPF7AzN5SHCEuw',
               team_id='T3QDD12QK', methods=['POST'])
def deny(**kwargs):    
    target = kwargs.get('text')
    py = subprocess.Popen(('/usr/bin/sudo sbin/hosts_deny.py %s' % target).split(), shell=False)
    py.wait(timeout=10)
    return slack.response(target + ' banned', response_type='in_channel')
