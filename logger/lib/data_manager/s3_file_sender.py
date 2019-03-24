from abc import ABCMeta, abstractmethod
from typing import Type
import threading
import s3fs


class S3FileSender:

    class ISaveFinishedCallback(metaclass=ABCMeta):

        @abstractmethod
        def on_save_finished(
            self,
            result: str
        ):
            raise NotImplementedError()

    class _DefaultSaveFinishedCallback(ISaveFinishedCallback):

        def on_save_finished(
            self,
            result: str
        ):
            pass

    def _s3_save_worker(
        self,
        local_filepath: str,
        s3_bucket_name: str,
        s3_filepath: str,
        callback
    ):
        try:
            fs = s3fs.S3FileSystem()
            fs.put(
                local_filepath,
                f's3://{s3_bucket_name}/{s3_filepath}'
            )
            result = 'OK'
        except Exception as e:
            result = e

        callback.on_save_finished(result=result)

    def __init__(
        self,
    ):
        pass

    def save2s3(
        self,
        local_filepath: str,
        s3_bucket_name: str,
        s3_filepath: str,
        callback: Type[ISaveFinishedCallback]=_DefaultSaveFinishedCallback()
    ):
        self._save2s3_async(local_filepath, s3_bucket_name,
                            s3_filepath, callback)

    def _save2s3_async(
        self,
        local_filepath: str,
        s3_bucket_name: str,
        s3_filepath: str,
        callback: Type[ISaveFinishedCallback]=_DefaultSaveFinishedCallback()
    ):
        threading.Thread(
            target=self._s3_save_worker,
            args=(
                local_filepath,
                s3_bucket_name,
                s3_filepath,
                callback
            )
        ).start()
