
from . import linux
from . import repo
import subprocess
from rich.console import Console
from rich.table import Table
from .url_filter import URLFilter


def update_repositories(verbose=False, oca=False, viraweb123=False, moonsunsoft=False, **kargs):
    print("Clone&Update Repositories")
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
        repo_detail['new_addons'] = repo_detail['current_addons'].difference(repo_detail['old_addons'])

    if verbose:
        linux.info_table(repos, ['workspace', 'name', 'state', 'new_addons'])




def show_repositories(verbose=False, oca=False, viraweb123=False, moonsunsoft=False, **kargs):
        # Generate filters
    repo_filter = False
    if oca or viraweb123 or moonsunsoft:
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


def show_module_info(version, workspace, **kargs):
    repo_module = []

    linux.info_table(repo_module, ['workspace', 'name', 'addons', 'Odoo16', 'Odoo17'])
  

####### show module info ########

def change_urls() -> list[str]:
    repos = repo.get_list() 
    urls_list = []
    for item in repos:
        workspace = item['workspace']
        name = item['name']
        url = f'https://github.com/{workspace}/{name}.git'
        urls_list.append(url)
        
    return urls_list
    

def supported_addons(version=False, **krgs):

    try:
        print('Loading...')
        repo_list = change_urls() 
        filter_url_list = URLFilter.public_filter_module(repo_list)
        get_repo = repo.get_addons_module(filter_url_list)
        url_fp = URLFilter.get_failed_urls()
        get_repo.extend(url_fp)
   
        table = Table("#", show_lines=True)
        table.add_column('Name')
        table.add_column('Workspace')
        table.add_column("Version : 16", justify="center")
        table.add_column("Version : 17", justify="center")
        table.add_column("Description")
        
        count=0

        for repo_item in get_repo:
            count += 1
            if repo_item.is_private == True and repo_item.status == 0:
                table.add_row( str(count), repo_item.name, repo_item.workspace, " ", " ", repo_item.description,style='bright_red', )
            else:
                if repo_item.versions_odoons[0] == '16.0' and repo_item.versions_odoons[1] == '17.0' :
                    table.add_row( str(count), repo_item.name, repo_item.workspace,  "✔", "✔", repo_item.description, style='bright_green', )
                elif repo_item.versions_odoons[0] == '16.0':
                    table.add_row( str(count), repo_item.name, repo_item.workspace,  "✔", '✗', repo_item.description,style='bright_green', )
                elif repo_item.versions_odoons[1] == '17.0':
                    table.add_row( str(count), repo_item.name, repo_item.workspace,  '✗', "✔", repo_item.description,style='bright_green', )

        console = Console()
        console.print(table)

    except Exception as e:  
        print(f"An error occurred: {str(e)}")
    
  
    

