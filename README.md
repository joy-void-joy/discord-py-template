Template for a discord bot

Usage
===
Fill .env with your own values (template in .env.default) and run the bot with ``python .``
The only feature the bot has at the beginning is "plz hello" which prints hello world

Debugging
===
NOTE: Those commands are only available in the authorized guilds by the authorized users (fill them in .env)

You can hot-load any module with:
```
plz load module
```
Replace module with the name of the file you want to load  
This plugs in any changes you have made without need to restart it.
You can just tap ``plz load`` to reload any loaded modules and ``plz clear`` to stop reloading them

You can debug by running your commands with:

```
plz run hello
```
Replace hello with your own command.
This will reload any loaded modules with the load commands and run your command. It will also display any errors directly in reply to you which is more convenient than switching back and forth.
Then you can just use ``plz run``
