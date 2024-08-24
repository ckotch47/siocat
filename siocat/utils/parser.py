import argparse

epilog_text = '''
        siocat --conf config_connection.json                                                : for connect server

'''

parser = argparse.ArgumentParser(
    description='Messaging program with socker.io server',
    epilog=epilog_text,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    '--conf',
    type=str,
    default=None,
    required=True,
    help='path for configuration json file'
)


m_arguments = parser.parse_args()