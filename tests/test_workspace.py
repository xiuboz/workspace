from workspace import __version__
from workspace.core import Workspace
from pathlib import Path

def test_version():
    assert __version__ == '0.1.0'


def test_basic():
    ws = Workspace('/tmp/workspace/test')
    assert ws.path() == Path('/tmp/workspace/test')


def test_chaining():
    ws = Workspace('/tmp/workspace/test0')
    assert ws.path() == Path('/tmp/workspace/test0')
    assert ws.subspace('test1').subspace('test2').path() == Path('/tmp/workspace/test0/test1/test2')

def test_str():
    ws = Workspace('/tmp/workspace/test')
    assert str(ws) == '/tmp/workspace/test'
    