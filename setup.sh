#!/bin/bash

if [[ "$1" == "env" ]]
then

    echo "Updating system ......"
    sudo yum -y update

    echo "Installing git ......"
    sudo yum -y install git

    echo "Downloading miniconda ......"
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

    echo "Installing miniconda ......"
    bash Miniconda3-latest-Linux-x86_64.sh -b

    echo "Cloning git repo ......"
    git clone https://github.com/hazel-gallery/demo_app.git

    echo "Install python package ......"
    miniconda3/bin/pip install -r demo_app/requirements.txt

elif [[ "$1" == "app" ]] 
then

    echo "Starting app ......"
    nohup miniconda3/bin/streamlit run demo_app/app.py > output.txt &

fi

echo "Done!"
