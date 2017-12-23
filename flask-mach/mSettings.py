class MSettings(object):
    def __init__(self):
        super()
        self._instance_path = '/Users/matt/workbench/shiny-engine/flask-mach/instance'

    @property
    def instance_path(self):
        return self._instance_path

    @instance_path.setter
    def instance_path(self, path):
        self._instance_path = path