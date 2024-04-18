#!/usr/bin/python3
"""
Python script that uses fabrics to create an archive of backup
"""
from fabric.api import local
from datetime import datetime

# - import the local command from fabric
# - create the func prototype
# - create the versions directory using
# - create the .tgz backup using tar


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
