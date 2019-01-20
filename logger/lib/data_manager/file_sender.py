from abc import ABCMeta, abstractmethod


class FileSender:

    def __init__(self):
        pass

    def save2s3(
        self,
        callback: FileSender.SaveFinishedCallback
    ):
        self._save_s3_async(callback)

    def _save_s3_async(
        self,
        callback: FileSender.SaveFinishedCallback
    ):
        result = '?'
        callback.on_save_finidhed(result=result)

    class SaveFinishedCallback(metaclass=ABCMeta):

        @abstractmethod
        def on_save_finidhed(
            self,
            result: str
        ):
            raise NotImplementedError()
