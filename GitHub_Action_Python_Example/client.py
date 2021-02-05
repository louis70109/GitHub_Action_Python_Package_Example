
class HelloWorld:

    def __init__(self,
                 message=None,
                 *args, **kwargs):
        super(HelloWorld, self).__init__(*args, **kwargs)
        self.message = message or 'Hello World!'

    def get_message(self):
        return self.message
