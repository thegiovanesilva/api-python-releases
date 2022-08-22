from fastapi import FastAPI

class App:
    def __init__(self) -> None:
        self.app = FastAPI()
    def get_app(self) -> FastAPI:
        return self.app