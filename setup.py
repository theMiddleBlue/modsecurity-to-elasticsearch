
from distutils.core import setup
from distutils.command.install import install
import distutils.archive_util
import os

class m2e_install(install):

    def touch(self, fname):
        if os.path.exists(fname):
            os.utime(fname, None)
        else:
            open(fname, 'a').close()

    def run(self):
        install.run(self)

        # Create the /var/log/modsecparser directory to be the default log directory
        distutils.archive_util.mkpath("/var/log/modsecparser", mode=0777)
        self.touch("/var/log/modsecparser/modsecparser.log")
        os.chmod("/var/log/modsecparser/modsecparser.log", 0777)

        distutils.archive_util.mkpath("/etc/modsecparser", mode=0o750)

        os.chmod("/etc/modsecparser/modsec_parser.py", 0775)
        os.chmod("/etc/modsecparser/parser.sh", 0775)

        os.chmod("/etc/default/modsecparserd.conf", 0640)

        os.chmod("/etc/init.d/modsecparserd", 0775)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="m2e - Modsecurity to elasticsearch",
    version="0.0.1",
    author="J3sux",
    author_email="jesux.dev@gmail.com",
    description="Modsecurity to elasticsearch package",
    url="https://github.com/theMiddleBlue/modsecurity-to-elasticsearch",
    data_files = [
        ('/etc/modsecparser/', [
            'modsec_parser.py',
            'parser.sh'
        ]),
        ('/etc/default/', [
            'modsecparserd.conf']),
        ('/etc/init.d/', [
            'modsecparserd'
        ])
    ],
    scripts=['modsec_parser.py'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    requires = [ 'elasticsearch (>= 1.22)' ],
    cmdclass={'install': m2e_install}
)