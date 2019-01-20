from abc import ABCMeta, abstractmethod


class FileRemover:

    def __init__(self):
        pass

    def remove(
        self,
        file_path: str,
        callback: FileRemover.RemoveFinishedCallback
    ):
        self._remove_async(callback)

    def _remove_async(
        self,
        file_path: str,
        callback: FileRemover.RemoveFinishedCallback
    ):
        result = '?'
        callback.on_remove_finidhed(result=result)

    class RemoveFinishedCallback(metaclass=ABCMeta):

        @abstractmethod
        def on_remove_finidhed(
            self,
            result: str
        ):
            raise NotImplementedError()
