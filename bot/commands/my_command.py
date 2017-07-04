from ..app import slack


@slack.command('ho', token='y1wAlkOznrGk6vBYsR7Hdn9n',
               team_id='T3QDD12QK', methods=['POST'])
def your_method(**kwargs):
    text = kwargs.get('text')
    return slack.response(text + '!', response_type='in_channel')

