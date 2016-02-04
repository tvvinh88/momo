from __future__ import absolute_import
from momo.backends.base import Document
import yaml


class BucketDocument(Document):
    """
    The BucketDocument class for the YAML backend.

    :param name: name of the bucket.
    :param path: path to the bucket document.

    """

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def load(self):
        """
        Load the bucket.

        :return: the loaded content.

        """
        with open(self.path) as f:
            return yaml.load(f.read())

    def dump(self, content):
        """
        Dump the content to the bucket file.
        """
        with open(self.path, 'w') as f:
            yaml.dump(content, f, default_flow_style=False)