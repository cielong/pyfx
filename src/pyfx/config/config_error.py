class ConfigurationError(Exception):
    def __init__(self, msg):
        super().__init__("Configuration Error: " + msg)
