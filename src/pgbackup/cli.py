from argparse import ArgumentParser, Action

knwon_drivers = ['s3', 'local']

class DriverAction(Action):
    # For more details check: https://docs.python.org/3/library/argparse.html#action
    # This test breaks a parser object into 2 values on 1 variable.
    # In this case, the variable name is driver, the values are local (or S3) and a path
    # So driver and destination are assigned from values
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver not in knwon_drivers:
            parser.error(f"Error: Unkown driver {driver}")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description='''Backup PostgreSQL databases locally
                                or to AWS S3.''')
    parser.add_argument("url", help="Database's URL to backup")
    parser.add_argument("--driver", help="How and where to store the backup",
                        nargs=2, action=DriverAction, required=True)
    return parser
