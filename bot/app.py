import importlib
import pkgutil


from flask import Flask
from flask_slack import Slack


app = Flask(__name__)
slack = Slack(app)

# XXX: commands/*.py import automatically.
for _, command, _ in pkgutil.walk_packages('.'):
    if command.startswith('bot.command'):
        print('%s load' % (command,))
        importlib.import_module(command)

app.add_url_rule('/', view_func=slack.dispatch)

if __name__ == "__main__":
    print('FLASK_APP=bot/app.py flask run -h 0.0.0.0')

