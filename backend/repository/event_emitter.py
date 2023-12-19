from typing import Dict, List, Callable


class EventEmitter:
    def __init__(self):
        self._callbacks: Dict[str, List[Callable]] = {}

    def on(self, event_name: str, function: Callable) -> Callable:
        if event_name not in self._callbacks:
            self._callbacks[event_name] = []
        self._callbacks[event_name].append(function)
        return function

    def emit(self, event_name: str, *args, **kwargs) -> None:
        for function in self._callbacks.get(event_name, []):
            function(*args, **kwargs)

    def off(self, event_name: str, function: Callable) -> None:
        if event_name in self._callbacks:
            self._callbacks[event_name].remove(function)
