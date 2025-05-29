# Genshin Daily Check-In

[![Docker Pulls](https://img.shields.io/docker/pulls/jogerj/genshin-daily-check-in)][dockerhub] [![Docker Stars](https://img.shields.io/docker/stars/jogerj/genshin-daily-check-in)][dockerhub]

[dockerhub]: https://hub.docker.com/r/jogerj/genshin-daily-check-in

This demo is created for educational purpose only.

## Docker setup

Set the configuration in `config.json` and use docker `docker compose up -d`.

### Configuring

Copy `config.json.example` as `config.json` and set the appropriate variables.

* Use a [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) using the `discord_webhook_url` variable. Otherwise it should be **left blank if unused**.
* You can set multiple users in the `users` array.
* Each user must have a username (any label), region (`os` for Global or `cn` for China), and [cookies set](#retrieving-cookie).
* `delay` is configured in seconds, meant for delay between user requests with `auto_claim` enabled. Should at least be 60 seconds to avoid GeeTest issues.
* To mention a user when daily login failed, add their user ID (enable developer settings in Discord, right click a user, and copy their user ID).
* The `auto_claim` flag is optional and can be set to `false` if the user doesn't opt for any cookies. The user will only receive a reminder by mention (if Discord user ID is set). The cookie and region of this user aren't evaluated.

### Retrieving cookie

1. Open developer console on the webpage (F12).
2. Go to the **Application** tab then click on **Cookies** on the side pane.
   * For Global: Select from the drop-down `https://act.hoyolab.com` and filter by `.hoyolab.com`
   * For China: Select from the drop-down `https://act.mihoyo.com` and filter by `.mihoyo.com`
3. Copy the values of these: `ltmid_v2`, `ltuid_v2`, `ltoken_v2`
4. Create a string of `key=value` pairs separated by a semi-colon `;` based on the token values like this:

   ```plaintext
   ltmid_v2=5I0Wqs5NYF_z6; ltuid_v2=12345678; ltoken_v2=v2_im7bvdBI21TtO4uPf145hotOYXWJDSw4JEIcsYrn1aH2S1FB6L4VfcoscoUlwnFVidTbqDR71rDe0wSdwTwEDscTgi7ocFj4CJxhG16Nz0Fpqmz7.VHPZyxo9EmN2.QysDH0UMNJ11PilULisMs54o-10AvJSkRHer6dU4Vst4BgCOGo2HCbUkZt6Bd1ZRb5K6PYfMe2Wb7vAJV2SdvY6dBNiCeC
   ```

5. Copy this string into the `config.json` file.
6. For any issues regarding retrieving cookies, see following [issue at genshin.py](https://github.com/thesadru/genshin.py/issues/151).

## Manual Setup

### Setup python virtual environment

   1. Create a new virtual environment `python -m venv .env` and activate the environment
      * Windows with PowerShell: `.env\Scripts\Activate.ps1`
      * Unix with bash: `source .env/bin/activate`)
   2. Install dependencies with `pip install -r requirements.txt`
   3. Configure `config.json` (see [above](#configuring))
   4. Test running the app `python src/main.py` and see if everything is correctly configured.
