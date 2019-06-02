# Demonstrate how to customize logging out
import logging

extraData = {
	'user': 'paavan014@gmail.com'
}
# TODO: add another function to log from


def anotherFunction():
	logging.debug('This is a debug-level message.', extra=extraData)


def main():
	# set the output file and debug level, and
	# TODO: use a custom formatting specification
	fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
	datestr = "%m/%d/%Y %I:%M:%S %p"
	logging.basicConfig(level=logging.DEBUG, filename='logs.log', format=fmtstr, filemode='a', datefmt=datestr)
	
	logging.info('This is an info-level log message.', extra=extraData)
	logging.warning('This is a warning-level message.', extra=extraData)
	anotherFunction()
	
	
if __name__ == '__main__':
	main()

