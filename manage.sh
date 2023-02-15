#!/bin/bash

if [[ "$1" == "env" ]]
then

    echo "Downloading miniconda ......"
    wget https://repo.continuum.io/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh

    echo "Installing miniconda ......"
    bash Miniconda3-py39_23.1.0-1-Linux-x86_64.sh

    echo "Install python package ......"
    miniconda3/bin/pip install -r demo_app/requirements.txt

elif [[ "$1" == "appup" ]] 
then

    echo "Starting up app ......"
    nohup miniconda3/bin/streamlit run demo_app/app.py > output.txt &

elif [[ "$1" == "appdown" ]] 
then

    echo "Shutting down app ......"
    sudo kill -9 $(sudo lsof -t -i:8501)

fi

echo "Done!"
