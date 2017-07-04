# Random Splash

A script that returns a random photo from [Unsplash](https://unsplash.com/).

## Installation

*Requires python2.7+*

Download the script to your ```$PATH```. 


## How to Use

1. Get a Client ID by making an app at [Unsplash Developers](https://unsplash.com/documentation#registering-your-application). 

2. Edit the *random_splash.py* script and insert your Client ID. The line should look like this:

	```
		CLIENT_ID = "" # Insert your Client ID HERE
	```

3. (Optional) You may Edit the ```COLLECTION_IDS``` to create a list of collections to pull photos from.

	```
		COLLECTION_IDS = ["145,658265,332,821,147,148,306253,142,855072,168631,256443,208422"]  # Choose a random photo from a list of collections
	```

	For example, this Unsplash Collection by called [Heads Up: https://unsplash.com/collections/**306253**](https://unsplash.com/collections/306253) has a Collection ID of **306253**.

	You can make your own list of Collections by adding them to a comma separated list. It will randomly select one from the collections. You can find [more Collections here](https://unsplash.com/collections/).

4. Run the script

	If all goes well, it should print a URL which can now be used for other scripts!




