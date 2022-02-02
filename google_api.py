from google.cloud import speech
import os
import io


class GoogleAPI:
    def __init__(self):
        # Creates google client
        self.client = speech.SpeechClient()

        # Full path of the audio file
        self.file_name = os.path.join(os.path.dirname(__file__), "test_recording.wav")

    def get_transcript(self):
        # Loads the audio file into memory
        with io.open(self.file_name, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            audio_channel_count=2,
            language_code="en-US"
        )

        # Sends the request to google to transcribe the audio
        response = self.client.recognize(request={"config": config, "audio": audio})

        # Reads the response
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))


