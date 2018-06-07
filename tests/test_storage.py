import tempfile
import pytest
from pgbackup import storage

@pytest.fixture
def infile():
    infile = tempfile.TemporaryFile('r+b')
    infile.write(b'Testing')
    infile.seek(0)
    return infile

def test_storing_file_locally():
    """
    Writes content from one file-like object to another.
    """
    infile = tempfile.TemporaryFile('r+b')
    infile.write(b'Testing')
    infile.seek(0)

    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing'

def test_storing_file_on_s3(mocker, infile):
    """
    Writes content from one readable to S3.
    """
    client = mocker.Mock()
    storage.s3(client,
            infile,
            "python-academy",
            "file-name")
    client.upload_fileobj.assert_called_with(
            infile,
            "python-academy",
            "file-name")
