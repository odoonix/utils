
from . import linux
from . import repo


def update_repositories(verbose=False, oca=False, viraweb123=False, moonsunsoft=False, **kargs):
    print("Clone&Update Repositories")
    # Generate filters
    filter = False
    if oca or viraweb123 or moonsunsoft:
        filter = []
        if oca:
            filter.append('oca')
        if viraweb123:
            filter.append('viraweb123')
        if moonsunsoft:
            filter.append('moonsunsoft')
    
    repos = repo.get_list(filter)
    for item in linux.progressBar(
            repos,
            prefix='Progress:',
            suffix='Complete',
            length=50):
        item['state'] = repo.git_update(item['workspace'], item['name'])

    if verbose:
        linux.info_table(repos, ['workspace', 'name', 'state'])
