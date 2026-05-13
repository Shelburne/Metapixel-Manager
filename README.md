# Metapixel-Manager
Tool for editing metapixel values for custom 'duck game' hats as .csv file.
## Background:
Making hats for duck game is pretty fun, and relatively easy compared to modifying other games.
All you have to do is make a .png and drop it into a folder, and you can even add more advanced functionality using metapixels.
Metapixels are the pixels occupying the rightmost column of a hat.png, each acts like a function. 
The red value of a pixel corresponds to the behavior (such as hat offset or particle lifetime), and the green and blue values are used as parameters.
This is an elegant solution, as it allows interesting features to be baked into hats without fiddling around with scripts or code, however it isn't perfect.

The main problem arises when you are tinkering with parameters and trying to get everyting to work just right. Let's say you want to modify your hat offset parameters, you either have to remember which pixel that corresponds to, or go through the metapixels in your editor with the color picker until you find which pixel has the red value 2. 

This tool allows you to instead modify your metapixels in a spreadsheet, where you can easily see all of the exact values, and then automatically convert them back into png format.

## Usage:
there are three ways to use the metapixel tool, single .csv extraction, batch .csv extraction, and metapixel overwrite.
### meta.csv Extraction
If you drag and drop an existing hat.png file onto duck_tool.exe, it will produce hat_meta.csv file, with values corresponding to the metapixels present in the hat file. Alternatively, by double clicking on the duck_tool.exe to run it as normal, you can create a hat_meta.csv for each hat.png in the Hats folder. 
Once you have created the hat_meta.csv, you can modify it using a spreadsheet software like excel.
### Save Metapixels.
Once you are satisfied with your values, you can put the values back into the hat. Simply drag and drop the hat_meta.csv onto the duck_tool.exe and a new hat.png will be produced in the Output folder for each hat.png in the Hats folder, with the metapixel values set to correspond to the used .csv
