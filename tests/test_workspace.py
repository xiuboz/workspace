from pathlib import Path

from workspace import __version__
from workspace.core import Workspace


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


def test_flatten():
    ws = Workspace('/tmp/workspace/test')
    ss = ws.subspace('subspace')
    ws.subpath('file1').touch()
    ws.subpath('file2').touch()
    ss.subpath('file3').touch()
    assert set(ws.flatten()) == {
        (('test', 'file1'), Path('/tmp/workspace/test/file1')),
        (('test', 'file2'), Path('/tmp/workspace/test/file2')),
        (('test', 'subspace', 'file3'), Path('/tmp/workspace/test/subspace/file3')),
    }
