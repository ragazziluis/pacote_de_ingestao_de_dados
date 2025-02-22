import boto3
import json
import os

class Storage:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def upload_to_s3(self, data: dict, filename: str):
        """Envia um arquivo JSON para um bucket S3."""
        try:
            json_data = json.dumps(data)
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=json_data,
                ContentType="application/json"
            )
            print(f"Arquivo {filename} enviado para o bucket {self.bucket_name}.")
        except Exception as e:
            print(f"Erro ao enviar arquivo para S3: {e}")
