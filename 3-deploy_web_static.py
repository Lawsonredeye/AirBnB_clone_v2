#!/usr/bin/python3
"""
script that creates and distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import local, run, put, env
from datetime import datetime
from os.path import exists

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
        run(f'ln -s /data/web_static/current {new_path}')
    except Exception as e:
        return False


def do_pack():
    """
    Fab function that creates an archive
    """
    Time = datetime.now()
    Time = Time.strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    result = local(f"tar -czvf versions/web_static_{Time}.tgz web_static")

    if result.succeeded:
        return (f"versions/web_static_{Time}")
    else:
        return None


def deploy():
    """
    Fabrics command which creates an archive an deploys it to a server
    without taking an argument
    """
    archive_path = do_pack()
    if archive_path.failed:
        return False
    do_deploy(archive_path)
