"""Administrator actions"""
import logging

from otoolbox import env
from otoolbox.repositories import linux
from otoolbox.repositories import repo

logger = logging.getLogger(__name__)


def update_repositories(verbose=False, oca=False, viraweb123=False, moonsunsoft=False, **kargs):
    logger.info("Clone&Update Repositories")
    # Generate filters
    repo_filter = False
    if oca or viraweb123 or moonsunsoft:
        repo_filter = ['odoo']
        if oca:
            repo_filter.append('oca')
        if viraweb123:
            repo_filter.append('viraweb123')
        if moonsunsoft:
            repo_filter.append('moonsunsoft')

    repos = repo.get_list(repo_filter)
    for repo_detail in linux.progressBar(
            repos,
            prefix='Progress:',
            suffix='Complete',
            length=50):
        branch_name = repo_detail.get('branch', None)
        repo_detail['old_addons'] = repo.get_addons_list(**repo_detail)
        repo_detail['state'] = repo.git_update(
            repo_detail['workspace'],
            repo_detail['name'],
            branch_name=branch_name)
        repo_detail['current_addons'] = repo.get_addons_list(**repo_detail)
        repo_detail['new_addons'] = repo_detail['current_addons'].difference(
            repo_detail['old_addons'])

    if verbose:
        linux.info_table(repos, ['workspace', 'name', 'state', 'new_addons'])


def show_repositories(verbose=False, oca=False, viraweb123=False, moonsunsoft=False, **kargs):
    # Generate filters
    repo_filter = False
    if oca or viraweb123 or moonsunsoft:
        repo_filter = ['odoo']
        if oca:
            repo_filter.append('oca')
        if viraweb123:
            repo_filter.append('viraweb123')
        if moonsunsoft:
            repo_filter.append('moonsunsoft')
    repos = repo.get_list(repo_filter)

    for repo_detail in linux.progressBar(
            repos,
            prefix='Progress:',
            suffix='Complete',
            length=50):
        repo_detail['addons'] = repo.get_addons_list(**repo_detail)

    linux.info_table(repos, ['workspace', 'name', 'addons'])
