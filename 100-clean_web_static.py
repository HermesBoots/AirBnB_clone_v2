#!/usr/bin/python3
"""Clean outdated releases from web servers"""


import fabric.api
import os


fabric.api.env.hosts = ['35.229.22.85', '34.74.166.73']
fabric.api.env.user = 'ubuntu'


def do_clean(number=0):
    """Clean outdated releases from web servers"""

    number = int(number)
    if number < 1:
        number = 1
    releases = sorted(os.listdir('versions'))[:-number]
    for archive in releases:
        fabric.api.local('rm versions/' + archive)
    command = 'ls -1 --directory '
    command += '/data/web_static/releases/web_static_* '
    command += '| sort --numeric-sort --reverse'
    releases = fabric.api.run(command).splitlines()[number:]
    for directory in releases:
        fabric.api.run('rm -rf /data/web_static/' + directory)
