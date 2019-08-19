#!/usr/bin/python3
"""Module to make tarball from a local directory"""


import datetime
import fabric.api
import os
import os.path


fabric.api.env.hosts = ['35.229.22.85', '34.74.166.73']
fabric.api.env.user = 'ubuntu'


def do_deploy(archive_path):
    """Upload a web site archive to a remote web server and install it"""

    if not os.path.exists(archive_path):
        return False
    path = fabric.api.put(archive_path, '/tmp/')[0]
    target = '/data/web_static/releases/' 
    target += os.path.splitext(os.path.split(path)[1])[0]
    fabric.api.run('mkdir -p ' + target)
    fabric.api.run('tar -xzf ' + path + ' -C ' + target)
    fabric.api.run('rm ' + path)
    fabric.api.run('mv ' + target + '/web_static/* ' + target + '/')
    fabric.api.run('rm -rf ' + target + '/web_static')
    fabric.api.run('rm -rf /data/web_static/current')
    fabric.api.run('ln -s ' + target + '/ /data/web_static/current')
    return True
