#!/usr/bin/python3
# deploy to my web server
from fabric import task
from fabric import Connection, SerialGroup
import os
from fabric.api import local, put, run, env


env.user = 'ubuntu'
env.hosts = ['54.157.137.104', '54.84.181.41']
@task
def do_deply(archive_path):
    """ Deploy """
    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')

    filename = os.path.basename(archive_path)
    folder_name = filename.split('.')[0]
    remote_path = '/data/web_static/releases/'

    conn.run('mkdir -p {}{}/'.format(remote_path, folder_name))
    conn.run('tar -xzf /tmp/{} -C {}{}/'.format(
        filename, remote_path, folder_name))

    run('rm /tmp/{}'.format(filename), warn=True)
    run('rm -rf {}'.format('/data/web_static/current/'))
    run('ln -s {} {}'.format('/data/web_static/current/', remote_path))
    print('New version deployed!')

    return True
