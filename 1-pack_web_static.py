#!/usr/bin/python3
# acompress files
from fabric.context_managers import path
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
	""" compress to a tar gzip file """
	time = datetime.utcnow()
	local("mkdir -p versions")
	save_to = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
								time.month,
								time.day,
								time.hour,
								time.minute,
								time.second)

	with path("web_static"):
		local("tar -czf {} web_static".format(save_to))
	return save_to
