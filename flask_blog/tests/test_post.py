# coding: utf-8
from .suite import BaseSuite


class TestPost(BaseSuite):
    def test_action(self):
        rv = self.client.get('/post/action')
        assert rv.status_code == 200