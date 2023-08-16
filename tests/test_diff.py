import pytest
import os
from gendiff.gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)

def get_diff_fixture():
    diff = open(get_fixture_path('diff'))
    return diff.read()

expected = get_diff_fixture()

@pytest.mark.parametrize("file1,file2", [('file1.json', 'file2.json'), ('file1.yml', 'file2.yml')])
def test_generate_diff(file1, file2):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected = get_diff_fixture()
    assert generate_diff(file1_path, file2_path) == expected

