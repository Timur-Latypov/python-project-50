import pytest
import os
from gendiff.gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

def get_diff_fixture(nesting):
    diff = open(get_fixture_path(nesting))
    return diff.read()

@pytest.mark.parametrize("file1,file2", [('plain1.json', 'plain2.json'), ('plain1.yml', 'plain2.yml')])
def test_plain(file1, file2):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected = get_diff_fixture('diff_plain')
    assert generate_diff(file1_path, file2_path) == expected

@pytest.mark.parametrize("file1,file2", [('nested1.json', 'nested2.json'), ('nested1.yml', 'nested2.yml')])
def test_plain(file1, file2):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected = get_diff_fixture('diff_nested')
    assert generate_diff(file1_path, file2_path) == expected
