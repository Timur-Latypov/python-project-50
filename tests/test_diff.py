import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def get_file1_path():
    return 'tests/fixtures/file1.json'

@pytest.fixture
def get_file2_path():
    return 'tests/fixtures/file2.json'

@pytest.fixture
def get_diff_path():
    diff = open('tests/fixtures/diff')
    return diff.read()


def test_diff(get_file1_path, get_file2_path):
    result = generate_diff(get_file1_path, get_file2_path)
    diff = open('tests/fixtures/diff')

    assert result == diff.read()
    # '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'