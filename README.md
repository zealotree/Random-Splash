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
COLLECTION_IDS = "145,658265,332,821,147,148,306253,142,855072,168631,256443,208422"  # Choose a random photo from a collection

3. (Optional) Edit the ```COLLECTION_IDS``` variable to specify a list of collections to pull a random photo.

	For example, this Unsplash Collection by called [Heads Up: https://unsplash.com/collections/**306253**](https://unsplash.com/collections/306253) has a Collection ID of **306253**.

	You can make your own list of Collections to pull from by adding them to a comma separated list. You can find [more Collections here](https://unsplash.com/collections/).

4. Run the script

If all goes well, it should print a URL which can now be used for other scripts!




