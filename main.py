import os

def check_git_installed():
    return_code = os.system('git --version')
    if return_code == 0:
        print("Git is installed.")
    else:
        print("Git is not installed.")

check_git_installed()
