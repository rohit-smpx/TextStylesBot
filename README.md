# FancyTextBot

Get fancy text styles for your Telegram Messages. With **live preview** of output as you type.

![Example Preview](./preview.png)

Deployed using [now-cli](https://zeit.co/).

---

## Run

### Dev Polling Mode

Run the _bot.py file

### Prod Webhook Mode

Set telegram bot webhook by:

```
https://api.telegram.org/bot{{BOT_TOKEN}}/setWebhook?url={{DEPLOYED_WEBHOOK_ENDPOINT}}
```

Deploy:

```sh
# If running first time:
# npm i -g now
# now login 
now
```

---

## Try me!

**Try it out by tagging [@fancy_text_bot](https://telegram.me/fancy_text_bot) on any chat screen on Telegram!**

### Currently supported text styles

- Z̸͙ͫ̕a̧̼̟͂̇l̢͉̉̀g̨̟̮͉͜ó̷̮ 
- bRoKeN CaPsLoCk
- 𝔻𝕠𝕦𝕓𝕝𝕖 𝕤𝕥𝕣𝕦𝕔𝕜
- 𝓒𝓾𝓻𝓼𝓲𝓿𝓮
- S P A C E D
- Ｆｕｌｌ－ｗｉｄｔｈ
- Ⓒⓘⓡⓒⓛⓔⓓ
- 🅝🅔🅖🅐🅣🅘🅥🅔 🅒🅘🅡🅒🅛🅔🅓
- 🄟⒜⒭⒠⒩⒯⒣⒠⒮⒤⒮
- 𝔉𝔯𝔞𝔨𝔱𝔲𝔯
- 1337 5p34k
- desreveR (Reversed)
- -- --- .-. ... . (Morse Code)
- ̶S̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶
- sᴍᴀʟʟ ᴄᴀᴘs
- Superˢᶜʳᶦᵖᵗ
- U̲n̲d̲e̲r̲l̲i̲n̲e̲
- Cebolinha (Changes Rs to Ls)

> **⚠️ WARNING**: Some styles will not work at all with special characters (*e.g. á, é, í, ó, ú*) since they rely on the existence of a unicode equivalent, which don't exist for most characters outside the A-Z and 0-9 scope.

> **⚠️ WARNING**: Telegram has forced result size limitations (around 260 characters), which means that long texts will be cut if they break this limit.

---

## Credits

Original project [TextStylesBot](https://github.com/eitchtee/TextStylesBot) by @eitchtee
