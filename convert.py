import os
import subprocess

def convert_mov_to_mp4(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'h264',
        '-crf', '23',  # adjust quality (0-51, 0 being lossless)
        '-preset', 'medium',  # adjust encoding speed vs. compression ratio
        '-c:a', 'aac',
        '-b:a', '128k',  # adjust audio bitrate as needed
        output_file
    ]
    subprocess.run(command)

def main():
    input_folder = 'input_folder'  # specify your input folder here
    output_folder = 'output_folder'  # specify your output folder here

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.mov'):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.rsplit('.', 1)[0] + '.mp4')
            print(f"Converting {input_file} to {output_file}")
            convert_mov_to_mp4(input_file, output_file)

if __name__ == "__main__":
    main()
