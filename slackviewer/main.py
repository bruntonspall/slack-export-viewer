import os

import click
import datetime

from slackviewer.archive import \
    extract_archive, \
    get_users, \
    get_channels, \
    compile_channels


def envvar(name, default):
    """Create callable environment variable getter

    :param str name: Name of environment variable
    :param default: Default value to return in case it isn't defined
    """
    return lambda: os.environ.get(name, default)


def flag_ennvar(name):
    return os.environ.get(name) == '1'


@click.command()
@click.option("-z", "--archive", type=click.Path(), required=True,
              default=envvar('SEV_ARCHIVE', ''),
              help="Path to your Slack export archive (.zip file)")
@click.option("-f", "--from-date", type=click.STRING, required=True,
              help="From date in ISO format - YYYY-MM-DD")
@click.option("-t", "--to-date", type=click.STRING, required=True,
              help="To date in ISO format - YYYY-MM-DD")
@click.option("-c", "--channel", type=click.STRING, required=True,
              help="Channel to select")
def main(archive, from_date, to_date, channel):
    if not archive:
        raise ValueError("Empty path provided for archive")

    path = extract_archive(archive)
    user_data = get_users(path)
    channel_data = get_channels(path)
    channels = compile_channels(path, user_data, channel_data)
    fromdate = datetime.date(*[int(x) for x in from_date.split("-")])
    todate = datetime.date(*[int(x) for x in to_date.split("-")])

    for message in channels[channel]:
        if message.datetime.date() >= fromdate and \
           message.datetime.date() <= todate:
            print "%s - %s: %s" % (message.username, message.time, message.msg)
