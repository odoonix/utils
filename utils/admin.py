
from . import linux
from . import repo


def update_repositories(verbose=False, **kargs):
    print("Clone&Update Repositories")
    repos = repo.get_list()
    for item in linux.progressBar(
            repos,
            prefix='Progress:',
            suffix='Complete',
            length=50):
        item['state'] = repo.git_update(item['workspace'], item['name'])

    if verbose:
        linux.info_table(repos, ['workspace', 'name', 'state'])
