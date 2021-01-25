# ComputerCraft-LocalHost
*Tested on Minecraft 1.16.3*

Tired of constantly uploading the same LUA file to pastebin every 5 seconds? This script allows you to upload LUA Files through a local webserver instead! All you need to do is save the file on your PC and the code updates instantly.

## Usage
The usage commands are exactly how they would be using pastebin but instead of an ID you use the PORT instead!
```
localhost get [PORT] [FILENAME]
localhost run [PORT] [ARGS]
```


## Installing
### Client
You can use ```pastebin get 9hLpCTHF localhost``` on your ComputerCraft Computer/Turtle in order to upload the client script to Minecraft.
Also, *You may need to [edit the ComputerCraft config files](#editing-computercraft-config-file) in order for this to work*.

### WebServer
I have included a python script in the [server folder](server/) in order to get your local server up and running. Any webserver script will do as long as it runs on `127.0.0.1` or `localhost` The python script runs on Python 3.7 and should run without needing to install any modules!


## Editing ComputerCraft Config File
If you haven't already you're going to need to edit the **computercraft-server.toml** *(Located in your save directory in the serverconfig folder!)* file to allow localhost connections! You will need to edit the action to *allow* if it is set to *deny*.
```
[[http.rules]]
		host = "127.0.0.0/8"
		action = "allow"
```

## Bug Reporting
Please report any bugs you may find [here](https://github.com/Breezy121/ComputerCraft-LocalHost/issues) :)
