import os
import glob
import tarfile

def extract_latest_model(models_dir='models'):
    # Get list of all tar.gz files in the models directory
    model_files = sorted(
        glob.glob(os.path.join(models_dir, '*.tar.gz')),
        key=os.path.getmtime,
        reverse=True
    )

    if not model_files:
        print("No models found to extract.")
        return

    latest_model = model_files[0]

    # Extract the latest model tar file
    with tarfile.open(latest_model, 'r:gz') as tar:
        tar.extractall(models_dir)

    print(f'Extracted {latest_model} to {models_dir}')

if __name__ == '__main__':
    extract_latest_model()
