#!/usr/bin/python3
"""
Python script that uses fabrics to create an archive of backup
"""
from fabric.api import local, run, put, env
from os.path import exists

# - using the do_pack guide
# - create the do_deploy()
# - if path to archive in local fails return False
# - else use put to upload the archive to the server to /tmp
# - Create a dir with run using
# => mkdir -p /data/web_static/releases/versions/web_static_{Time}
#  use run and tar -xczf to uncompress the archive into a folder in =>
# - /data/web_static/releases/versions/web_static_{Time}
# - create sym link
# => ln /data/web_static/releases/versions/web_static_{Time}
#  to /data/web_static/current
# - env.hosts = ['52.86.247.182', '52.91.128.2']
# - env.user = 'ubuntu'

env.user = 'ubuntu'
env.hosts = ['52.86.247.182', '52.91.128.2']


def do_deploy(archive_path):
    """
    Fab command used to deploy an archive into a remote server
    """
    if not exists(archive_path):
        return False
    archive = archive_path[9:-4]
    new_path = f"/data/web_static/releases/{archive}"
    try:
        run('mkdir -p /tmp/versions')
        put(archive_path, '/tmp/versions')
        run(f'mkdir -p /data/web_static/releases/{archive}')
        run(f'tar -xvf /tmp/{archive_path} -C {new_path}')
        run(f'rm -rf /tmp/{archive_path}')
        run(f'rm -rf /data/web_static/current')
        run(f'mkdir -p /data/web_static/current')
        # run(f'ln -sf /data/web_static/current {new_path}')
        run(f'ln -sf  {new_path} /data/web_static/current')
    except Exception as e:
        return False
