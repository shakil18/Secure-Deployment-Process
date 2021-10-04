import os
import re
import time

from pygit2 import clone_repository

CLONE_PATH = '/home/client-app/repo'


# adjust repo address / url
def repo_address_adjust(repo):
    try:
        # url includes https (e.g. https://github.com/shakil18/testrepo)
        if re.search('https://', repo):
            adjusted_address = re.sub('https://', ':x-oauth-basic@', repo)

        # url without https (e.g. github.com/shakil18/testrepo)
        else:
            adjusted_address = ':x-oauth-basic@' + repo
        return adjusted_address

    except Exception as err:
        print(err)


# cloning client-repo
def pull_repo(token, url):
    repo_access_url = 'https://' + token + url

    # printing for log
    # print(f'\n=====> Access Token: {token} <====='
    #       f'\n=====> Repo Address: {repo_access_url} <=====')

    clone_repository(repo_access_url, CLONE_PATH)

    print('\n====> Client repo cloned successfully! <====')


if __name__ == '__main__':
    # get data from session-environment variables
    access_token = os.getenv('USER_ACCESS_TOKEN')
    repo_address = repo_address_adjust(os.getenv('USER_GIT_REPO'))

    start_time = time.time()
    pull_repo(access_token, repo_address)

    print("=====> Pull repo: %s milliseconds <=====" % ((time.time() - start_time) * 1000))
