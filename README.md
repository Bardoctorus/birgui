<h1>Bardoctorus' Simple Image Resizer, Now With 56% More GUI!</h1>

This is an extension of the [command line image converter](https://github.com/Bardoctorus/bardoctorus_batch_image_resizer) I made partly out of convenience as a writer (After the 7000th time opening Photoshop <em>just to resize a fu-</em>) and partly to learn Python by hacking things together.

The command line version was fine. Kinda. It worked for every use case I had, because I only ran it in folders with image files. I later found out that Photoshop files kill the program. I also found out that a surprising number of techy people found adding the script to their PATH and running the program from the terminal to be out of their comfort zones.

Hence the addition of PySimpleGui

<h2>Shiny knobs</h2>

The GUI is staying as simple as possible for now. Choose a folder, choose a new width in pixels. No options, no nonsense. That said there are some quality of life things to add.

<h2>TODO</h2>

This list will likely change over time, but the main features I want to add:

- Confirmation/Failure message on completion ("x files created, y failures)
- Option to create a log file
- Basic how-to and contact address to send logs to

There are also some things I need to rework:

- File handling: don't try to open any files that aren't image files
- Error reporting: Only report failed saves, previous step should help with this
- How to return consistent information to the user (command line/GUI parity)

Things to think about:

- Creating versions for Win/Lin/Mac (VMs?)
- Beta testers
- Trimming the repository (actually using gitignore, making dependency files etc)