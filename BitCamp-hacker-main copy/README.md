# Sign Language Detector Python

# Workshop 1: [Here](https://github.com/BigThinkAI-UMD/workshop1)

# Workshop 2: Set up the repository and dependencies
## HEAVILY RECOMMEND ATTENDING THIS WORKSHOP IF INTERESTED IN THIS PROJECT. THIS MAKES TROUBLESHOOTING EASIER.
A repository is just a collection of code that you worked on and are storing it some place for others to see. For all projects, using Github and repositories is necessary for showing your progress over time and a history of all the updates you have worked on throughout your project. Below is some of the necessary dependencies. **WE ARE ASSUMING THAT YOU HAVE PYTHON AND PIP INSTALLED!** These are necessary to download the dependencies below. If you do not have them installed, please google how to install:

        1. Python
        2. Pyenv or Conda
        3. Pip
        4. Homebrew (optional but helpful)

It's recommended to use a virtual environment like points 2 and 3 above to manage dependencies. If installation isn't working, try `python3` or `pip3` instead. **How to install the venv (virtual environment is later below.**

### If you do **NOT** have "git" installed PLEASE INSTALL IT TOO. INSTRUCTIONS BELOW
#### Introduction

Git is a free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. This guide will walk you through the steps to install Git on your system.

#### Installation Steps

#### Windows
1. **Download Git Installer:** [Visit the official Git website](https://git-scm.com) and download the latest version of Git for Windows.
2. **Run the Installer:** Once the download is complete, run the installer by double-clicking the downloaded file.
3. **Configure Installation Settings:** Follow the installation wizard, selecting the desired options. The default settings are usually sufficient for most users.
4. **Complete Installation:** Once the installation is complete, you can verify the installation by opening a command prompt and typing: `git --version`. This should display the installed Git version.

#### macOS
1. **Install Git via Homebrew** (recommended): If you have Homebrew installed, you can install Git by running the following command in the terminal: `brew install git`
2. **Install Git from [Git website](https://git-scm.com):** Alternatively, you can download the latest Git installer for macOS from the official Git website.
3. **Run the Installer:** Once the download is complete, run the installer by double-clicking the downloaded file.
4. **Configure Installation Settings:** Follow the installation wizard, selecting the desired options. The default settings are usually sufficient for most users.
5. **Complete Installation:** After installation, you can verify Git installation by opening a terminal and typing: `git --version`. This should display the installed Git version.

#### Linux
1. Install Git via Package Manager:
**Ubuntu/Debian:**
```
sudo apt-get update
sudo apt-get install git
```
**Fedora:**
`sudo dnf install git`
**Arch Linux:**
`sudo pacman -S git`
2. **Complete Installation:** Once the installation is complete, you can verify Git installation by opening a terminal and typing: `git --version`. This should display the installed Git version.

Now that we have git, navigate to the folder/directory that you want your code to be located on your computer using the `cd [directory name here]` command. `cd` means "change directory", or switch into that folder. If you want to pop back/exit the folder, use `cd ..`. Using these commands, run this code to clone the repo and have the repo template on your computer:

https://github.com/BigThinkAI-UMD/BitCamp-hacker

`git clone https://github.com/BigThinkAI-UMD/BitCamp-hacker`
[Link to repo to clone here](https://github.com/BigThinkAI-UMD/BitCamp-hacker)

Also, here is a .zip file of all the data you will need to build the model. It is too large to directly add to the Github repo linked above, so please download it and keep it in the same folder/directory/workspace as the rest of your files. [UPDATED_Data.zip](https://drive.google.com/file/d/1VrKK2v_x-wAZJviP-K5dNdrRyJspyYm8/view?usp=sharing)

## Setup Python Virtual Environment (venv)

Setting up a Python virtual environment is essential to isolate your project's dependencies from the system-wide Python installation. Follow these steps to create and activate a virtual environment for this project. Please use **Python 3.10.11** (others may work, this is just what we used). We suggest using conda. For installation instructions click either [conda](https://docs.anaconda.com/free/anaconda/install/index.html) or [pyenv](https://pypi.org/project/penv/)

### 1. Create Virtual Environment

**For Pyenv:**

Open a terminal or command prompt and navigate to your project directory. Then, execute the following command to create a virtual environment named `venv`:

`python -m venv venv` (Again try python3 if that doesn't work)

This command will create a folder named *venv* in your project directory, which will contain the Python interpreter and libraries specific to your project.

**For Conda:**

Create a new virtual environment with the following command. When conda asks you to proceeed press 'y':

`conda create --name <my-env> python=3.10`

### 2. Activate Virtual Environment
Activate the virtual environment using the appropriate command based on your operating system:
**For Pyenv:**
**For Windows:**

`.\venv\Scripts\activate`

**For macOS and Linux:**

`source venv/bin/activate`

After activation, you should see (venv) prefixed in your terminal prompt, indicating that the virtual environment is active.

**Conda:**
Then, you can activate the command with the following command:

`conda activate <my-env>`

**ONCE DONE WORKING, YOU DEACTIVATE THE ENVIRONMENT BY RUNNING `deactivate`**

To deactivate, with conda run:

`conda deactivate`

## Dependencies

This project requires the following dependencies to be installed:

Now, it is time to install the necessary dependencies.

**Run `pip install -r requirements.txt`**

You can also install the dependinces manually, please install the packages below using the **same version**

opencv-python==4.7.0.68
mediapipe==0.9.0.1
scikit-learn==1.2.0

## Running `collect_imgs.py`

Note: When you are running `collect_imgs.py`, make sure you have created a data folder in the project to hold the images.

Here you will have to hold each sign language character for 20 seconds (remember we are skipping j and z). The code will take a 100 images from that 20 seconds and store it. Make sure you have good lighting, so we have good training data!

## How to make sure you are done!
- By the end, you should have a virtual environment with the dependencies mentioned installed. Also, please have this repository cloned locally. 

# Workshop 3: We will process the data, code will be released after the workshop!

# Workshop 4: We will train and use our model, code will be released after the workshop!

Credits: [![Watch the video]](https://www.youtube.com/watch?v=MJCSjXepaAM)
