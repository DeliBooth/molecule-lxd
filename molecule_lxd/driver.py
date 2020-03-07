from __future__ import absolute_import

from molecule import logger
from molecule.api import Driver

log = logger.get_logger(__name__)


class LXD(Driver):
    """
    LXD Driver Class.

    The class responsible for managing `LXD`_ containers.  `LXD`_ is not
    the default driver used in Molecule.

    Molecule leverages Ansible's `lxd_container`_ module, by mapping
    variables from ``molecule.yml`` into ``create.yml`` and ``destroy.yml``.

    .. _`docker_container`: https://docs.ansible.com/ansible/latest/docker_container_module.html
    .. _`Docker Security Configuration`: https://docs.docker.com/engine/reference/run/#security-configuration
    .. _`Docker daemon socket options`: https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option
    """  # noqa

    def __init__(self, config=None):
        """Construct LXD."""
        super(LXD, self).__init__(config)
        self._name = "lxd"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def login_options(self, instance_name):
        return {"instance": instance_name}

    def ansible_connection_options(self, instance_name):
        return {"ansible_connection": "lxd"}

    def login_cmd_template(self):
        return 'lxc exec {instance} bash'
