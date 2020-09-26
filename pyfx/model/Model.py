import json


class Model:
    def __init__(self,
                 controller: "Controller"
                 ):
        self._controller = controller

    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except Exception as e:
            self._controller.exit(e)
