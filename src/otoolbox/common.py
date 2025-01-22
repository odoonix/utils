




def add_repo_list_filter(parser):
    parser.add_argument(
        '--oca',
        default=False,
        action='store_true')
    parser.add_argument(
        '--no-oca',
        dest='python',
        action='store_false')

    parser.add_argument(
        '--viraweb123',
        default=False,
        action='store_true')
    parser.add_argument(
        '--no-viraweb123',
        dest='python',
        action='store_false')

    parser.add_argument(
        '--moonsunsoft',
        default=False,
        action='store_true')
    parser.add_argument(
        '--no-moonsunsoft',
        dest='python',
        action='store_false')
