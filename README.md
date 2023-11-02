# UC Guest Wi-Fi Reconnection Script
## Overview
This Python script is designed to assist Line Computers (with Chrome Browsers) in automatically reconnecting to the UC Guest Wi-Fi network. The script provides a convenient solution for Line Computers that have temporary connections to this network, ensuring a smooth and hassle-free reconnection process. Please utilize Windows' Task Scheduler to automate this process.

## Features
- The script offers the following features:

- Wi-Fi Disconnection: It disconnects the Line Computer from the current Wi-Fi network, preparing it for reconnection.

- Wi-Fi Reconnection: It establishes a connection to the "UC Guest" Wi-Fi network, allowing the Line Computer to regain network access.

- Automated Form Submission: The script automatically fills out a guest access form to ensure seamless network access, particularly if the UC Guest network requires form submission for authentication.

- Logging: Detailed logging of actions and results to track the success and status of each step.

## Usage

- The script will automatically attempt to pip install necessary packages. Please ensure Python is installed for this to work.

- In case that the guest wifi form changes, please alter these details to customize your needs:
    - network_name: Name of the Wi-Fi network to connect to (e.g., "UC Guest").
    - target_url: The URL you want to reach after successfully reconnecting.
    - website_link: The URL of the guest access form, if applicable.
    - username, email, and phone: Guest form information.
- Run the script (.exe file) to automate the disconnection, reconnection, and guest form submission. Set up in Task Scheduler to automate this process every day.
- Check the logs in the wifi_login.log file to verify the success and status of each step.

## Error Handling
The script is designed to handle errors and provide detailed logs for troubleshooting. It logs errors, timeouts, and failures to help you diagnose any issues that may arise during the reconnection process. If any questions or major bugs arise, please contact me at halim.choi@lgsolutionpartner.com with the log file attached.

###### Created by Halim Choi (LG Solution Partner LLC @ Ultium Cells)
