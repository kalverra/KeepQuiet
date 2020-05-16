# Keep Quiet
My gaming setup is right next to our bedroom, and during some late night, wine-fueled sessions, I can get a little loud, keeping up my fiancée. So I built this python script to keep my sound level in check. It uses sound device and numpy to monitor how many decibels I'm currently producing into my microphone, and plays an audio file of said fiancée telling me to be quiet. Also a notification, which I may or may not remove.

While the programming in this is fairly simple, it did teach me a bit about how sound works and is measured. Check out this article on how decibels work: https://www.scienceabc.com/pure-sciences/why-negative-decibels-are-a-thing.html

### Running
`python keep_quiet.py` 

Simple enough, I have a windows task to automatically start running the program at 8PM.

### TODO and Known Issues
* The microphone is right next to my mouth most times, so sometimes things like direct breath into it will interfere and give a false positive. This seems to be a hardware issue though, not sure what I can do programmatically to prevent this.
* Adding more thresholds and alerts for different levels, like a warning level
