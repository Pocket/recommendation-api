import logging
import pickle
from io import BytesIO
import os

import boto3


class ModelLoader:
    """
    Loads and deserializes a model
    """
    def load(self, path: str):
        raise NotImplemented

    def get_size(self, path: str) -> int:
        raise NotImplemented


class LocalLoader(ModelLoader):
    def load(self, path: str):
        with open(path, 'rb') as f:
            return pickle.load(f)

    def get_size(self, path: str) -> int:
        return os.path.getsize(path)


class S3Loader(ModelLoader):
    def __init__(self, bucket):
        self._bucket = bucket

    def load(self, path: str):
        logging.info(f'Loading a model from s3, bucket: {self._bucket}, path: {path}')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self._bucket)
        object = bucket.Object(path)

        file_stream = BytesIO()
        object.download_fileobj(file_stream)

        return pickle.loads(file_stream.getvalue())

    def get_size(self, path: str) -> int:
        s3_client = boto3.Session().client('s3')
        response = s3_client.head_object(Bucket=self._bucket, Key=path)
        return response['ContentLength']
