# -*- coding: utf-8 -*-

"""
author: Lorenzo Cerrone
"""
from scpw import scpw


class TestSCPW:
    def test_main(self):
        assert scpw.main() is None
