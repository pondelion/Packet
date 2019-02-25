from abc import ABCMeta, abstractmethod
from typing import Type


class FileRemover:

    class IRemoveFinishedCallback(metaclass=ABCMeta):

        @abstractmethod
        def on_remove_finished(
            self,
            result: str
        ):
            raise NotImplementedError()

    class _DefaultRemoveFinishedCallback(IRemoveFinishedCallback):

        def on_remove_finished(
            self,
            result: str
        ):
            pass

    def __init__(self):
        pass

    def remove(
        self,
        file_path: str,
        callback: Type[IRemoveFinishedCallback]=_DefaultRemoveFinishedCallback()
    ):
        self._remove_async(callback)

    def _remove_async(
        self,
        file_path: str,
        callback: Type[IRemoveFinishedCallback]=_DefaultRemoveFinishedCallback()
    ):
        result = '?'
        callback.on_remove_finidhed(result=result)
