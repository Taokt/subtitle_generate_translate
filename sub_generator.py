import sys
import torch
import numpy as np
import os
import glob
import whisper
from whisper.utils import write_srt


def run(input_path: str, output_path: str) -> None:
    get_subs(input_path, output_path)
    # trans_subs(output_path)


def get_subs(input_path: str, output_path: str) -> None:
    # Use gpu if the device have one
    
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
  
    # Load the model
    model = whisper.load_model("base", device=DEVICE)

    # Creat path to store resulting subtitles
    output_path = os.path.join(output_path , "English_subtitles")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Create subs
    for filename in glob.glob(os.path.join(input_path, "*.mp4")):
        result = model.transcribe(filename)
        current_path = os.path.join(output_path , os.path.basename(os.path.splitext(filename)[0]+'.srt')) 
        with open(current_path, "w", encoding="utf-8") as srt_file:
            write_srt(result["segments"], file=srt_file)


def main() -> None:
    if len(sys.argv) != 3:
        print(
            "Error: Invalid number of arguments.\n"
            "Usage: python sub_generator.py <input-path> <output-path>\n"
            "Example: python sub_generator.py ...\folder_that_contains_videos ...\folder_that_save_subs"
        )
        sys.exit(1)

    run(input_path=sys.argv[1], output_path=sys.argv[2])


if __name__ == "__main__":
    main()
