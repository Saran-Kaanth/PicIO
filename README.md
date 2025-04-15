# PicIO💫

PicIO is an AI-powered tool that extracts images from given files and provides descriptions for each corresponding image. It supports four different file formats and can handle multiple file uploads within the same format. With the power of Ollama's vision models, PicIO generates descriptive text for the images extracted from the documents.

## Features

- **Extracts images from PDF, Word, Excel, and PowerPoint files.**
- **Generates descriptions for the extracted images using Gemma3 Model (Multimodal) from Ollama.**
- **Supports multiple file uploads of the same format.**
- **Flexible to handle large files for image extraction.**
- **Provides fallback model for generating descriptions when the primary model fails.**

## Python Version

- Python 3.11 or higher

## Installation

To install the required dependencies for PicIO, run:

```bash
pip install -r requirements.txt
```

### MultiModel Used for Generating Descriptions

1. **gemma3:4b** (Default model)

Above model is used to generate descriptions for the images extracted from your documents.

### Running Gemma3 Models Locally

To use Gemma3 models locally, you need to install [**Ollama**](https://ollama.com/) on your system.

After installing Ollama, open your command prompt and run the following command to pull the model:

```bash
ollama run gemma3:4b
```

## Usage

1. **Upload Files**: You can upload multiple files of the same format (PDF, Word, Excel, PowerPoint) for image extraction and description generation.

2. **Extract Images**: The tool will extract images from the uploaded files.

3. **Generate Descriptions**: Descriptions for each image will be generated and displayed.

## Demo

You can access the demo recording of the tool here: [Demo](https://drive.google.com/file/d/1AAqiyUrGuKrmzfQ_YDrppSM1NmhCA0id/view?usp=drive_link)


## Sample Files

The sample data/files that is demoed in the recording can be found in the `data` folder of the repository. These files are provided for you to test and explore the functionality of PicIO.


## License

MIT License


## Get Started

Try out PicIO today and see how it can help you extract and describe images from your documents. Explore the demo, test with the sample files, and start using the tool!

To run the application, simply execute:

```bash
streamlit run app.py
```