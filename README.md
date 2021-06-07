# 3310 Composer
## A script similar to the composing app on Nokia 3310

The script only uses the builtin libraries of Python. The interface is pretty self-explainatory, but it can be explained like this:

- **File Name**: The source of notes. The notes should be written in this file.
- **Pace**: The pace of the sound. It's calculated like `120/Pace notes per second`, so, for example, 60 is 1 note per second and 120 is 2 notes per second. Default is 120.
- **Bitrate**: Bitrate of the output file. Higher bitrate is needed for higher-pitched sounds. The quality of the audio is usually proportional to the bitrate; however, the improvement of quality is inversely proportional to the bitrate. Thus, there is a great difference between 1000 bps and 2000 bps, but the difference between 4000 bps and 44100 bps is usually neglectable, especially in lower-pitched audio. Please don't forget that higher bitrate means bigger files. Default is 2048.
- **Frequency of A4**: In Western music, all the notes are defined as their relation to the note A4 (or La 4), so this option lets you change the **base** pitch of the notes. Default is 440.
- **Start Conversion**: Starts conversion? Please note that as the program is single-threaded, the interface freezes between the beginning and the end of the conversion.
- After the conversion, a green text is shown right under the **Start Conversion** button, telling the size of the output file. If an error occurs while converting, it's shown as red text in the same place.
