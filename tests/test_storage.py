import pytest
from pacote_de_ingestao_de_dados.meu_pacote.storage import Storage

@pytest.fixture
def storage():
    return Storage(bucket_name="meu-bucket-de-teste")

def test_upload_to_s3(storage, mocker):
    mock_s3 = mocker.patch("boto3.client")
    storage.upload_to_s3({"teste": "dados"}, "teste.json")
    mock_s3.put_object.assert_called_once()
