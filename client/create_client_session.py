import os
import subprocess
import time
import uuid

CLIENT_SESSION_FILE_PATH = os.path.abspath(os.getcwd())

# TODO: used for evaluaiton
SERVICE_PROVIDER_PATH = os.path.abspath(os.path.join('../service_provider'))
ENV_SESSION_FILE_PATH = SERVICE_PROVIDER_PATH + '/env_session'

SCONE_CAS_ADDR = "5-4-0.scone-cas.cf"


def create_client_session(access_token, repo):
    start_time = time.time()

    # read session_template.yml and create_session.yml file
    try:
        read_session_template = open(CLIENT_SESSION_FILE_PATH + '/client-session.yml', 'r')
        create_client_session = open(CLIENT_SESSION_FILE_PATH + '/session.yml', 'w')

        # generate session-id
        session = str(uuid.uuid4())

        # TODO: used for automation of evaluation
        os.system(f"echo export SESSION='\"{session}\"' >> {ENV_SESSION_FILE_PATH}")

        # replace placeholders
        check_words = ('$SESSION', '$ACCESS_TOKEN', '$GIT_REPO')
        replace_words = (session, access_token, repo)

        for line in read_session_template:
            for check, rep in zip(check_words, replace_words):
                line = line.replace(check, rep)
            create_client_session.write(line)

        read_session_template.close()
        create_client_session.close()

        subprocess.run("chmod +x client_certificate", shell=True)
        subprocess.run("source client_certificate", shell=True, executable="/bin/bash")

        # send client_session file to CAS server
        os.system(
            f"curl -k -f --cert client.pem  --key client-key.pem  --data-binary @session.yml -X POST 'https://{SCONE_CAS_ADDR}:8081/session'")

        print('\n=====> Session has created successfully! <=====')
        print(f'\n=====> Your Session-ID: {session} <=====')

    except FileNotFoundError as e:
        print(f'=====> Client-session file not found! <=====')

    # TODO: for evaluation, counted in milliseconds
    end_time = (time.time() - start_time) * 1000
    with open(SERVICE_PROVIDER_PATH + '/automated_dep_eval.txt', 'a') as file:
        file.write(f'Create client_session: {end_time} milliseconds\n')
    print(f"=====> Create client_session: {end_time} milliseconds <=====")


# main function
if __name__ == '__main__':
    # providing user credential and repo through user_input()
    # access_token = getpass('Access Token: ')
    # repo = input('Repo HTTPS Address (e.g. https://github.com/user/project): ')

    access_token = '96a0f18054ea6bab782b2f8383d77625c4a60aed'
    repo = 'https://github.com/shakil18/testrepo'
    # repo = 'https://github.com/shakil18/helloworld'

    create_client_session(access_token, repo)
