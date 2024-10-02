import sys

# There is now only one logger.
class Logger:
    def __init__(self, filters, handlers):
        self.filters = filters
        self.handlers = handlers

    def log(self, message):

        if len(self.filters) > 0:
            filter_match = (f.match(message) for f in self.filters)
        else:
            filter_match = None

        print(self.log.__qualname__)

        try:
            iter(filter_match)
            print(*filter_match,sep='\n')
        except:
            print("filter is not iter")
            return


        if all(f.match(message) for f in self.filters):
            for h in self.handlers:
                h.emit(message)

# Filters now know only about strings!

class TextFilter:
    def __init__(self, pattern):
        self.pattern = pattern

    def match(self, text):
        return self.pattern in text

# Handlers look like “loggers” did in the previous solution.

class FileHandler:
    def __init__(self, file):
        self.file = file

    def emit(self, message):
        self.file.write(message + '\n')
        self.file.flush()


ferr = TextFilter('Error')
fwarn = TextFilter('Warn')
fcrit = TextFilter('Critical')
finform = TextFilter('Inform')

h = FileHandler(sys.stdout)
logger = Logger([ferr,fwarn,fcrit,finform], [h])

logger.log('Ignored: this will not be logged')
logger.log('Error: this is important')
logger.log('Test??')
logger.log('Inform: this is Inform')
logger.log('Warn: this is Warn')
