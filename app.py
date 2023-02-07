import streamlit as st
import os
import subprocess
from PIL import Image
import shutil


app_mode = st.sidebar.selectbox(
    "Choose the app mode",
    ["Welcome", "Backgournd Remover"]
)


def bgr(img_path, output_path):
    '''background remove'''
    res = subprocess.run(
        'backgroundremover -i {} -o {}'.format(
            img_path, output_path
        ),
        shell = True,
        capture_output = True
    )

def purge_folder(folder_path):
    for f in os.listdir(folder_path):
        os.remove(os.path.join(folder_path,f))        

def format_file_name(file_name):
    fname = file_name.split('.')[0]
    ftype = file_name.split('.')[1]
    fname2 = ''.join(e for e in fname if e.isalnum())
    return fname2 + '.' + ftype
    


def save_buffered(buffered_file,buffered_folder):
    # save the streamlit buffered files to temp folder
    if os.path.isdir(buffered_folder) == False:
        os.mkdir(buffered_folder)
    with open(os.path.join(buffered_folder,buffered_file.name),"wb") as f:
        f.write(buffered_file.getbuffer())

if app_mode == "Welcome":
    st.write('Welcome')

elif app_mode == "Backgournd Remover":
    st.title("Background Remover")
    st.markdown('''
        Intro here
    ''')
    files = st.sidebar.file_uploader(
        label = "Upload images", 
        accept_multiple_files = True
    )
    btn = st.sidebar.button('Upload')
    if btn:
        purge_folder('temp/')
        purge_folder('outputs/')
        for fi in files:
            fi.name = format_file_name(fi.name)
            save_buffered(fi,'temp/')
        files = os.listdir('temp/')
        for fi in files:
            src_path = 'temp/' + fi
            fo = fi.split('.')[0] + '.png'
            dest_path = 'outputs/' + fo 
            bgr(src_path, dest_path)
            image = Image.open(dest_path)
            rotated_image = image.rotate(angle=270)
            st.image(rotated_image)
            rotated_image.save(dest_path)

        cwd = os.getcwd()
        shutil.make_archive(
            base_name = cwd + '/outputs', 
            format = 'zip',
            root_dir = cwd,
            base_dir = 'outputs',
        )
        with open("outputs.zip", 'rb') as f:
            st.sidebar.download_button('download as zip',f,file_name='bgr_images.zip')
        os.remove('outputs.zip')
