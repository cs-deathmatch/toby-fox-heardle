# mario-heardle

**DISCLAIMER: If you want to play this legitimately, don't go snooping in main.js - you'll spoil yourself if you do!**

This is a clone of [Sonic Heardle](https://sonic-heardle.glitch.me/), which is a clone of [Joywave Heardle](https://joywave-heardle.glitch.me) (which in turn was modeled on <a href="https://www.heardle.app/" title="Heardle">Heardle</a> and <a href="https://heardle-kpop.glitch.me/" title="Heardle">K-Pop Heardle</a>) that is focused on Mario.

Each Mario Heardle is randomly chosen from one of several songs from the video game franchise.

Following this paragraph is a tutorial for aspiring Heardle makers, completely unedited from [Joywave Heardle's original README.](https://glitch.com/edit/#!/joywave-heardle?path=README.md) I made this site by following their instructions. (They themselves were relying on [WJSN Heardle's](https://github.com/haseul/wjsn-heardle) code, editing it for their own project. I figured I should state this for the record.)
 <br /> 
 <br /> 
HOW TO MAKE YOUR OWN HEARDLE (UDPATED on 4/17/22)

1. Remix this project to create your own copy of the code
2. Rename the project with the URL that you'd like to Heardle to live at
3. Open the **index.html** file & replace **"Joywave"** with the artist/genre of your heardle
4. In the **index.html** file, you can update the image that gets shared with your link by updating lines **23-33**.

(Items 5-10 are all edits to the **main.js file**)

5. On line **2** of **main.js** file and update **artist** with the **artist/genre** of your heardle - This will update all the text boxes & titles where "Joywave" shows up
6. On line **3** of **main.js** file, update **twitter** with your own twitter or instagram handle - This will update the contact info and replace every instance of "joywavez"
7. On line **4** of **main.js**, update the **startDate** to the current date in the format **YEAR-MONTH-DAY (YYYY-MM-DD)** - This will start the counter for your Heardle
8. On line **5** of **main.js**, "const **Cn**" is initialized. Replace the text with a list of song titles that you want to show up as options in your Heardle. It should follow the format **"Song - Artist".** Make sure each song is in quotes and has a comma after it
9. On line **78** of **main.js**, "**On**" is initialized. Here you'll have to replace the links with links to your songs. Only Soundcloud links at the moment. Each link will have to follow the following format:
   `{ url: "<link>", answer: "Song - Artist" },`
10. The order of the songs in "const Cn" should match the order in "On".
11. If you want your heardle link to show up whenever someone shares their results, on **line 4831** remove the "**//**" and update the link with your own heardle link

<br /> 
<br />

At the moment, the order of the songs match the order that the Heardle's will appear, so if you dont want to ruin the surprise, have someone else upload the order of the songs and links for you!
<br />

Glitch auto saves your code, so your changes should be available as soon as the code is editted.
<br />

Heardle doesnt work in the "Open Preview Pane" option, so make sure to view it in the "Preview in new window" option
<br />
<br />

Feel free to tweet/dm me @joywavez on twitter if you have any issues/questions!
