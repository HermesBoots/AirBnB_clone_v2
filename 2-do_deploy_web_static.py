#!/usr/bin/python3
"""Module to make tarball from a local directory"""


import datetime
import fabric.api
import os
import os.path


fabric.api.env.hosts = ['35.229.22.85', '34.74.166.73']


def do_deploy(archive_path):
    """Upload a web site archive to a remote web server and install it"""

    if not os.path.exists(archive_path):
        return False
    file = os.path.splitext(os.path.split(archive_path)[1])[0]
    path = fabric.api.put(archive_path, '/tmp/' + file)
    if path.failed:
        return False
    path = path[0]
    target = '/data/web_static/releases/' + file
    if fabric.api.run('mkdir -p ' + target).failed:
        return False
    if fabric.api.run('tar -xzf ' + path + ' -C ' + target).failed:
        return False
    if fabric.api.run('rm ' + path).failed:
        return False
    if fabric.api.run('mv ' + target + '/web_static/* ' + target + '/').failed:
        return False
    if fabric.api.run('rm -rf ' + target + '/web_static').failed:
        return False
    if fabric.api.run('rm -rf /data/web_static/current').failed:
        return False
    if fabric.api.run('ln -s ' + target + '/ /data/web_static/current').failed:
        return False
    return True
