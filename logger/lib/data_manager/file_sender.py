from abc import ABCMeta, abstractmethod


class FileSender:

    def __init__(self):
        pass

    def save2s3(
        self,
        callback=FileSender._DefaultSaveFinishedCallback(): FileSender.SaveFinishedCallback
    ):
        self._save_s3_async(callback)

    def _save_s3_async(
        self,
        callback=FileSender._DefaultSaveFinishedCallback(): FileSender.SaveFinishedCallback
    ):
        result = '?'
        callback.on_save_finished(result=result)

    class SaveFinishedCallback(metaclass=ABCMeta):

        @abstractmethod
        def on_save_finished(
            self,
            result: str
        ):
            raise NotImplementedError()

    class _DefaultSaveFinishedCallback(FileSender.SaveFinishedCallback):

        def on_save_finished(
            self,
            result: str
        ):
            pass
