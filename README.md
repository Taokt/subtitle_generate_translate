# subtitle generating from video and translate the result into other languages i.e. Chinese
## Subtitle video generating: initial implementation 
Automatically generate subtitles from video and save them to srt format by using whisper

## Translate to other languages : TODO:

## Installation: TODO

## Usage: to be complete
The program is able to process multiple videos that is saved under a folder, and export the resulting srt files under the specified folder with a new folder, with the corresponding srt subtitle file has the same name as the original video
To run the program, if , for example , your videos are saved with the path "C:\your_videos", and you would like the result to be saved under "C:\your_videos"
run the program with 'py sub_generator.py C:\your_videos C:\your_videos'
The result will be saved to C:\your_videos\English_subtitles, you don't have to create English_subtitles folder yourself, it will be automatically generated