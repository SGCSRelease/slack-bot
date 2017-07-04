from ..app import slack


@slack.command('say', token='RpIpHsyeLOzCMyMZkcMwPHdH',
               team_id='T3QDD12QK', methods=['POST'])
def your_method(**kwargs):
    text = kwargs.get('text')
    return slack.response(text, response_type='in_channel')

