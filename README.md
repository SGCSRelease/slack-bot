# slack ban bot

- TODO: Why? What for?


## Install

- TODO: How?
- python3
- perhaps venv & `pip install -r requirements.txt`


## Run
- `FLASK_APP=bot/app.py flask run -h 0.0.0.0 --debugger --reload`

```
 * Serving Flask app "bot.app"
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

- Expose port (and Link to custom domain)

## Link to Slack
- Slack > Manage Apps > Custom Integrations > Slash Commands > Add Configuration
    - For every [*slash commands*](https://github.com/SGCSRelease/slack_bot/tree/master/bot/commands):
        - Command: `{your_command}`
        - Method: `POST`
        - Custom URL (http://{exposed_domain}:{exposed_port}/)
    - Generated tokens (and Team Id) should be injected to [./bot/commands/{command}.py]( https://github.com/SGCSRelease/slack_bot/blob/master/bot/commands/hosts_deny.py#L6).


### Auto Run

- TODO: How?


## Features

- /etc/hosts.deny $ip
    - add hosts.deny $ip - Done
    - remove hosts.allow $ip

- /etc/hosts.allow $ip
    - add hosts.allow $ip
    - remove hosts.deny $ip  

- /usr/bin/whois $ip
    - country info return
- /sbin/iptables -D $ip
    - ?
- /help


## /etc/sudoers
```
bot    ALL=(root) NOPASSWD: /home/bot/slack_bot/sbin/
```

