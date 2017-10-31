import subprocess

from watchdog.events import FileSystemEventHandler


class Fail2BanLogModifiedHandler(FileSystemEventHandler):
    def process(self, event):
        print(event.src_path, event.event_type)

        if event.src_path == './test.log':
            banOverlappingFails(event.src_path)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


def banOverlappingFails(src_path):
    ip = findNewBannedIp(src_path)
    if not ip:
        return
    else:
        # Check if new banned ip is overlapped
        # there are two options
        # 1. search /var/log/fail2ban.log everytime
        # 2. make my own banned ip history file
        pass

    # hosts_deny process
    add_py = subprocess.Popen(('/usr/bin/sudo sbin/add_ip.py %s %s'
        % ('/etc/hosts.deny', ip)).split(), shell=False)
    add_py.wait(timeout=10)

    remove_py = subprocess.Popen(('/usr/bin/sudo sbin/add_ip.py %s %s'
        % ('/etc/hosts.allow', ip)).split(), shell=False)
    remove_py.wait(timeout=10)


def findNewBannedIp(src_path):
    # open file 'fail2ban.log' and find newly banned ip
    log_file = open(src_path)
    log_lines = log_file.read().split('\n')
    log_file.close()

    log_length = len(log_lines)

    if not log_lines[log_length-1]:  # FIXME: Don't know why '' at the end
        log_lines.pop()
        log_length -= 1

    new_line = log_lines[log_length-1].split(' ')
    line_length = len(new_line)

    if not new_line[line_length-2] == 'Ban':
        ip = None

    else:
        ip = new_line[line_length-1]

    return ip
