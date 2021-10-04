import os
import shutil
import subprocess
import time

from flask import Flask, request, redirect, render_template, send_file

SERVICE_PROVIDER_PATH = os.path.abspath(os.path.join('../service_provider'))

SESSION_TEMPLATE_FILE = '/client-session.yml'
ENV_SESSION_FILE_PATH = SERVICE_PROVIDER_PATH + '/env_session'
RETRY_DEPLOY_MAX = 3

print("Service_provider_path: ", SERVICE_PROVIDER_PATH, "\nSession ENV:", ENV_SESSION_FILE_PATH)

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def service_home():
    return render_template('index.html')


# Download API
@app.route('/download_template_session/')
def download_template_session():
    start_time = time.time()

    print("Current working_path: ", subprocess.run("ls"))

    # create a session file for client with MrEnclave, FSPF_Tag, and FSPF_Key
    subprocess.run("chmod +x bundle_scripts.sh", shell=True, cwd=SERVICE_PROVIDER_PATH)
    subprocess.run("source bundle_scripts.sh", shell=True, executable="/bin/bash", cwd=SERVICE_PROVIDER_PATH)

    # copy generated client_session file to web_service directory
    source = SERVICE_PROVIDER_PATH + SESSION_TEMPLATE_FILE
    destination_dir = os.path.abspath(os.path.join(os.getcwd(), "session_files"))

    if os.path.exists(destination_dir):
        os.rmdir(destination_dir)
        os.makedirs(destination_dir)
    else:
        os.makedirs(destination_dir)

    destination = os.path.abspath(os.path.join(destination_dir + SESSION_TEMPLATE_FILE))
    print("Source_path: " + source + "\nDestination_path: " + destination)

    shutil.copy(source, destination)

    file_path = destination
    print("File_path: " + file_path)

    end_time = ((time.time() - start_time) * 1000)
    print(f"=====> Download session_template: {end_time} milliseconds <=====")
    with open(SERVICE_PROVIDER_PATH + '/automated_dep_eval.txt', 'a') as file:
        file.write(f'Download session_template: {end_time} milliseconds\n')

    return send_file(file_path, as_attachment=True, attachment_filename=None)


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
@app.route('/upload_client_session/', methods=['GET', 'POST'])
def upload_client_session():
    # start_time = time.time()
    pull_repo_returncode = 1
    las_deploy_returncode = 1

    if request.method == 'POST':
        client_session_id = request.form['session_id']
        # check if the session_id is not provided
        if client_session_id == '':
            print('~~~~~ No Session-ID is given! ~~~~~')
            return redirect(request.url)
        # check if the session-id is valid/ do next process
        else:
            # update env_session with client_session_id
            os.system(f"echo export SESSION='\"{client_session_id}\"' >> {ENV_SESSION_FILE_PATH}")
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

            print(f'=====> Client Session-ID: {client_session_id} <=====')
            return f'Session-ID: {client_session_id}'

    # end_time = ((time.time() - start_time) * 1000)
    # with open(SERVICE_PROVIDER_PATH + '/automated_dep_eval.txt', 'a') as file:
    #     file.write(f'Upload session_template: {end_time} milliseconds\n')
    #
    # print(f"=====> Upload session_template: {end_time} milliseconds <=====")

    return redirect('/')


# Clean the system
@app.route('/cleanup_system/', methods=['GET'])
def clean_system():

    # clean-up system
    subprocess.run("sh cleanup_system.sh", shell=True, executable="/bin/bash", cwd=SERVICE_PROVIDER_PATH)
    print(f'=====> Clean-up system <=====')
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
