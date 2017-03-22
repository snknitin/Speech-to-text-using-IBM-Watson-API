# Speech-to-text-using-IBM-Watson-API
Transcribing lecture videos to create subtitles or closed captions

Watson Documentation

https://www.ibm.com/watson/developercloud/speech-to-text/api/v1/#recognize_sessionless_nonmp12

# Step 1 — Get the IBM Bluemix credentials
  Sign up to get the Username and password and create an app with the Watson service and select Speech to text to use the API
# Step 2 — Getting the transcript
  Intall the SDK
 $ pip install watson-developer-cloud


# Support

The interfaces support the following Input features:

-> Languages: Supports Brazilian Portuguese, French, Japanese, Mandarin Chinese, Modern Standard Arabic, Spanish, UK English, and US English.

-> Models: For most languages, supports both broadband (for audio that is sampled at a minimum rate of 16 KHz) and narrowband (for audio that is sampled at a minimum rate of 8 KHz) models.

-> Audio formats: Transcribes Free Lossless Audio Codec (FLAC), Linear 16-bit Pulse-Code Modulation (PCM), Waveform Audio File Format (WAV), Ogg format with the opus codec, mu-law (or u-law) audio data, or basic audio.

-> Audio transmission: Lets the client pass as much as 100 MB of audio to the service as a continuous stream of data chunks or as a one-shot delivery, passing all of the data at one time. With streaming, the service enforces various timeouts to preserve resources.


# Results

> Song similarity  0.329525483304     - Eminem - Rap God (Explicit)

> Speech similarity  0.975907288808   - Charlie Chaplin - Final Speech from The Great Dictator
