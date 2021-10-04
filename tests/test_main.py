from polarity.__main__ import Args


def test():
    thing = Args(args=['-t TEST'])
    args, unknown = thing.parser.parse_known_args()
    assert args.test == 'test help'
