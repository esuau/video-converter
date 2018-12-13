# Video Converter

This program converts video files to AVI format from an Amazon S3 bucket as it pulls message from Google Cloud Pub/Sub. 
Additionally, it performs item updates on a DynamoDB table.

## Requirements

### Credentials

Make sure you have credentials for both AWS and Google Cloud :

**AWS**

The credentials for Amazon Web Services are stored in the file `~/.aws/credentials`.

**Google Cloud**

The credentials are stored in a `.json` file. The environment variable `GOOGLE_APPLICATION_CREDENTIALS` defines the 
location of this file on your computer. You can set it as follows:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
``` 

### Dependencies

**Python dependencies**

Install required dependencies with the following command:
```bash
pip install -r requirements.txt
```

**FFmpeg**

The converter uses FFmpeg to perform media file conversion. Please [download it](https://www.ffmpeg.org/download.html)
and add the executable to your `PATH` variable.

## Execution

If every requirement is completed, you can run the project as shown below:
```bash
python conversion_worker.py
```