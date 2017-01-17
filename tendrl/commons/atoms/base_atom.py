import abc

import six

from tendrl.commons.atoms.exceptions import AtomNotImplementedError


@six.add_metaclass(abc.ABCMeta)
class BaseAtom(object):
    def __init__(
            self,
            name,
            enabled,
            help,
            inputs,
            outputs,
            uuid,
            parameters
    ):
        self.name = name
        self.enabled = enabled
        self.inputs = inputs
        self.help = help
        self.outputs = outputs
        self.uuid = uuid
        self.parameters = parameters
        self.etcd_server = self.parameters['etcd_server']
        self.config = self.parameters['config']
        self.manager = self.parameters['manager']

    @abc.abstractmethod
    def run(self):
        raise AtomNotImplementedError(
            'define the function run to use this class'
        )
