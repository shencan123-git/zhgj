# *_*coding:utf-8 *_*
import unittest
class Meta(type):
    def __new__(cls, name, parents, attrs):
        LONG = 4
        id = 1
        _attrs = {}
        for k, v in attrs.items():
            if k.startswith('test_'):
                id_str = str(id).zfill(LONG)
                _k = k.replace('test_', 'test_{}_'.format(id_str))
                _attrs[_k] = v
                id += 1
            else:
                _attrs[k] = v
        return type.__new__(cls, name, parents, _attrs)

class _TestCase(unittest.TestCase,metaclass=Meta):
    pass