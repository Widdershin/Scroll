import unittest

from scroll import entity


class TestBaseEntity(unittest.TestCase):
    """The tests for entity.BaseEntity"""

    def test_class_creates(self):
        test_entity = entity.BaseEntity()
        assert(test_entity)
