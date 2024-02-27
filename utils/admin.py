
from . import linux
from . import repo


def update_repositories(verbose=False, oca=False, viraweb123=False, moonsunsoft=False, **kargs):
    print("Clone&Update Repositories")
    # Generate filters
    filter_module = False
    if oca or viraweb123 or moonsunsoft:
        filter_module = []
        if oca:
            filter_module.append('oca')
        if viraweb123:
            filter_module.append('viraweb123')
        if moonsunsoft:
            filter_module.append('moonsunsoft')
    
    repos = repo.get_list(filter_module)
    for item in linux.progress_bar(
            repos,
            prefix='Progress:',
            suffix='Complete',
            length=50):
        item['state'] = repo.git_update(item['workspace'], item['name'])

    if verbose:
        linux.info_table(repos, ['workspace', 'name', 'state'])
