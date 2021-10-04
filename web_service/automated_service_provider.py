import os
import subprocess
import time

SERVICE_PROVIDER_PATH = os.path.abspath(os.path.join('../service_provider'))

SESSION_TEMPLATE_FILE = '/client-session.yml'
ENV_SESSION_FILE_PATH = SERVICE_PROVIDER_PATH + '/env_session'
RETRY_DEPLOY_MAX = 3

print("Service_provider_path: ", SERVICE_PROVIDER_PATH, "\nSession ENV:", ENV_SESSION_FILE_PATH)


# execute las docker image
def las_deploy():
    status_service_las = subprocess.run("source service_las.sh", shell=True, executable="/bin/bash",
                                        cwd=SERVICE_PROVIDER_PATH)
    time.sleep(15)
    return status_service_las.returncode


# execute pull_repo docker image
def pull_repo_deploy():
    status_service_pull_repo = subprocess.run("source service_pull_repo.sh", shell=True,
                                              executable="/bin/bash",
                                              cwd=SERVICE_PROVIDER_PATH)
    time.sleep(10)
    return status_service_pull_repo.returncode


# deploy into kubernetes cluster
def kubernetes_deploy():
    status_kubernetes_deploy = subprocess.run("source kubernetes_deploy.sh", shell=True,
                                              executable="/bin/bash",
                                              cwd=SERVICE_PROVIDER_PATH)
    return status_kubernetes_deploy.returncode


# Upload API
def deploy():
    pull_repo_returncode = 1
    las_deploy_returncode = 1

    retry_las = 1

    # profiling pulling client-repo
    start_time = time.time()
    while retry_las <= RETRY_DEPLOY_MAX:
        las_deploy_returncode = las_deploy()

        if las_deploy_returncode == 0:
            print("~~~~~ Success at Las! ~~~~~")

            retry_pull_repo = 0
            while retry_pull_repo <= RETRY_DEPLOY_MAX:
                pull_repo_returncode = pull_repo_deploy()
                if pull_repo_returncode == 0:
                    print("~~~~~ Success at Pull-repo! ~~~~~")

                    end_time = ((time.time() - start_time) * 1000)
                    with open(SERVICE_PROVIDER_PATH + '/automated_dep_eval.txt', 'a') as file:
                        file.write(f'Pulling client-repo: {end_time} milliseconds\n')
                    print(f"=====> Pulling client-repo: {end_time} milliseconds <=====")
                    break
                else:
                    print("~~~~~ Pull-repo service is in loading... ~~~~~")
                    retry_pull_repo += 1
            break
        else:
            print("~~~~~ Las service is in loading... ~~~~~")
            retry_las += 1

    if retry_las == RETRY_DEPLOY_MAX and las_deploy_returncode != 0:
        print("~~~~~ Error at Las! ~~~~~")
    if las_deploy_returncode == 0 and pull_repo_returncode != 0:
        print("Error at Pull-repo!")

    if las_deploy_returncode == 0 and pull_repo_returncode == 0:
        print("~~~~~ Deploying into Kubernetes! ~~~~~")
        kubernetes_deploy()

    print(f'=====> Done! <=====')


# Clean the system
def clean_system():
    # clean-up system
    subprocess.run("sh cleanup_system.sh", shell=True, executable="/bin/bash", cwd=SERVICE_PROVIDER_PATH)
    print(f'=====> Clean-up system <=====')


if __name__ == "__main__":
    deploy()
