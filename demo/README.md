# Demo

## Disclaimer
This demo is created for educational purpose only.


## Docker setup

For ease of use, just set the configuration and use docker `docker compose up -d`.
When updating the configuration, add the `--build` flag at the end of command from step to rebuild the container.

## Manual Setup

### Configuring

Copy `config.json.example` as `config.json` and set the appropriate variables.
* Use a [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) using the `discord_webhook_url` variable. Otherwise it should be **left blank if unused**.
* You can set multiple users separated by new key-value pair.
* Each user must have a username (any label), region (`os` or `cn`), and cookies set.
* `delay` is configured in seconds, meant for delay between user requests with `auto_claim` enabled.
* To mention a user when daily login failed, add their user ID (enable developer settings in Discord, right click a user, and copy their user ID).
* The `auto_claim` flag is optional and can be set to `false` if the user doesn't opt for any cookies. The user will only receive a reminder by mention (if Discord user ID is set). The cookie and region of this user aren't evaluated.
* The cookie token can be retrieved by opening [this webpage](https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481) page and opening console (F12). Run `document.cookie` and copy the text returned.\
    
### Setup python virtual environment

   1. Create a new virtual environment `python -m venv .env` and activate the environment 
      * Windows with PowerShell: `.env\Scripts\Activate.ps1`
      * Unix with bash: `source .env/bin/activate`)
   2. Install dependencies with `pip install -r requirements.txt`
   3. Test running the app `python src/main.py` and see if everything is correctly configured.

