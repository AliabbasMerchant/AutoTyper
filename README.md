# AutoTyper
An auto-typer program, with the ability to provide custom input

## Inspiration:
[hackertyper.net](https://hackertyper.net)  
[pyautogui](https://github.com/asweigart/pyautogui)  
[VSCode HackerTyper Extension](https://marketplace.visualstudio.com/items?itemName=jevakallio.vscode-hacker-typer)

## Requirements:
`pyautogui` and its dependencies

## Usage:
`auto_typer.py file_name`  
The contents of the file `file_name` will be auto typed.  

The contents of the file are read.  
After a 1 second pause at the beginning, the text is auto-typed, with a pause of `MILLISECONDS_TO_SLEEP` milliseconds between 2 letters.

## Safe Zone:
The auto typer will not auto type anything, if the mouse cursor is in this area of the screen.  
The limits of the safe zone can be tweaked (See Config)

## Config:
* `MILLISECONDS_TO_SLEEP`: The number of milliseconds to sleep after typing each letter.
* `SAFETY`: The limits of the safe zone at the upper left corner of the screen.
* `DEBUG`: If true, logs are printed on the terminal.

## Disclaimer:
Please **DO NOT** use this for unethical/illegal/immoral purposes.
