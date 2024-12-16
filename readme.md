# XTTS Audio Generator

This project allows you to generate audio files using the XTTS-v2 model from Hugging Face, with your own audio recordings as the base. It leverages the XTTS model to recreate voices from provided samples and generate audio based on text input.

## Requirements

- Python 3.10
- Pip
- A machine with an internet connection to download the TTS model

## Installation and Setup

### 1. Clone the Repository

Start by cloning the repository to your local machine using Git:

```bash
git clone https://github.com/Ethan04Munoz/XTTS_audio_generator.git
```

### 2. Install Dependencies

Navigate to the cloned directory and run the following command to install the necessary dependencies:

```bash
python gitClone.py
```

This will clone the XTTS model repository into the appropriate folder. After that, drag and drop `generate.py` into the newly created folder.

### 3. Organize Your Files

Inside the root folder (where the `generate.py` script is located), create two folders:
- `examples`: Store your audio samples here (at least 6 seconds long, preferably longer). The files should be in `.wav` format.
- `output`: The generated audio will be saved here.

### 4. Install TTS Package

Before running the script, install the `TTS` package by running the following command:

```bash
pip install TTS
```

### 5. Run the Script

Now, you are ready to run the audio generation script. Open a command prompt or terminal inside the root folder and execute the following:

```bash
python generate.py
```

### 6. First Time Setup

If it's the first time you're running the script, it will begin downloading the XTTS model, which might take a few minutes depending on your internet connection.

### 7. Generate Your Audio

Once the model is downloaded, the program will prompt you to input the text that you want the generated audio to say. You will also be asked to provide other parameters. Follow the instructions to generate the audio file.

The generated audio will be saved in the `output` folder.

## Troubleshooting

- **Error during model download**: Ensure you have a stable internet connection and sufficient disk space.
- **Issues with audio format**: Make sure your audio samples in the `examples` folder are in `.wav` format and at least 6 seconds long for optimal results.
