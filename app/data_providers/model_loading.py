import logging
import pickle
from io import BytesIO

import boto3


class ModelLoader:
    """
    Loads and deserializes a model
    """
    def load(self, path: str):
        raise NotImplemented


class LocalLoader(ModelLoader):
    def load(self, path: str):
        with open(path, 'rb') as f:
            return pickle.load(f)


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
