import requests
from . import repo
from .addons_model import AddonsModel 

class URLFilter:
    failed_urls = []
    list_failed_urls: AddonsModel = [] 

    @staticmethod
    def public_filter_module(urls_filter: list[str]) -> list:
        list_filter_urls = []
        for url_f in urls_filter:
            try:
                response = requests.get(url_f, timeout=20)
                if response.status_code == 200:
                    list_filter_urls.append(url_f)
                else:
                    URLFilter.failed_urls.append(url_f)  

            except requests.exceptions.Timeout:
                URLFilter.failed_urls.append(url_f)  

            except requests.exceptions.RequestException as e:
                URLFilter.failed_urls.append(url_f)  
        
        return list_filter_urls


    @staticmethod
    def get_failed_urls() -> list[AddonsModel]:
        for url in URLFilter.failed_urls:
            get_name = repo.get_name_module(url)
            get_workspace = repo.get_workspace_module(url)
            ad_model = AddonsModel(
                workspace=get_workspace,
                  description='Failed Repository. It may be a private repository!',
                  name=get_name,
                  versions_odoons=['16.0', '17.0'],
                  is_private = True,
                  status=0  
                    )
            URLFilter.list_failed_urls.append(ad_model)

        return URLFilter.list_failed_urls

    