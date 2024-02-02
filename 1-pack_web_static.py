#!/usr/bin/python3
# compress files
from fabric.api import local
import datetime import datetime


def do_pack():
    time = datetime.utcnow()
    local("mkdir -p versions")
    save_to = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
                                                            time.month,
                                                            time.day,
                                                            time.hour,
                                                            time.minute,
                                                            time.second)

    local(f"tar -czf {save_to} web_static")
    return save_to
