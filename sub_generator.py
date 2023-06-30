import sys
import torch
import numpy as np
import os
import whisper
from whisper.utils import write_srt


def run(input_path: str, output_path: str) -> None:
    # Use gpu if the device have one
    torch.cuda.is_available()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # Load the model
    model = whisper.load_model("base", device=DEVICE)
    print(
        f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
        f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
    )
    result = model.transcribe(input_path)

    with open(output_path, "w", encoding="utf-8") as srt_file:
        write_srt(result["segments"], file=srt_file)


def main() -> None:
    if len(sys.argv) != 3:
        print(
            "Error: Invalid number of arguments.\n"
            "Usage: python sub_generator.py <input-path> <output-path>\n"
            "Example: python sub_generator.py 'video.mp4' 'subtitle.srt'"
        )
        sys.exit(1)

    run(input_path=sys.argv[1], output_path=sys.argv[2])


if __name__ == "__main__":
    main()
