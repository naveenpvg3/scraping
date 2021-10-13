#Scraping From API

Object: a python code to extract data of the given Telegram channel’s username. The extracted data includes channel id, channel title, channel date if the channel has geolocation, channel bio, the number of channel participants/subscribers.
Telegram channels username list: [‘nytimes_world’, ‘washingtonpost', ‘CNNBrk', ‘WorldNews', ‘bloomberg', ‘Political_News'] <example>
Output: a CSV file of a data frame that includes all the required variables. 

##Tips about the Telegram platform:
Telegram channels: are a tool for broadcasting your public messages to large audiences. They offer a unique opportunity to reach people directly, sending a notification to their phones with each post. Telegram Channels can have an unlimited amount of subscribers, and only admins have the right to post. For example, media organizations and public figures use channels to stay in touch with their readers, voters and fans. 

##Prerequisites of getting API:
Install the Telegram app on your computer 
Register an account using the phone number in Telegram: https://my.telegram.org/auth
Get your Telegram API credentials: to connect to Telegram, you need an api_id and an api_hash. You need to log in to Telegram core and go to the API development tools area to get these parameters. Fill out the form, and you can receive api_id and api_hash. Here is Telegram’s help documentation about how to get your API credentials.

##Packages installation:
You need python 3 installed.
You can use the Telethon package on your system using the terminal command: pip install telethon
Telethon documentation can be found at https://docs.telethon.dev/en/latest/index.html 
