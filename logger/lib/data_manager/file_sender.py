from abc import ABCMeta, abstractmethod
from typing import Type


class FileSender:

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

    def __init__(self):
        pass

    def save2s3(
        self,
        callback: Type[ISaveFinishedCallback]=_DefaultSaveFinishedCallback()
    ):
        self._save2s3_async(callback)

    def _save2s3_async(
        self,
        callback: Type[ISaveFinishedCallback]=_DefaultSaveFinishedCallback()
    ):
        result = '?'
        callback.on_save_finished(result=result)
