

# Google APIs Setup

## Enabling APIs

From the [Google APIs Dashboard](https://console.cloud.google.com/apis/dashboard) page, search for and "enable" any API(s) of interest (like Google Sheets API).

## Service Account Credentials

To interface with the enabled Google APIs, the app will need access to a local "service account" credentials file.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account, and give it a name. Grant the service account access to the project via a "Basic" > "Editor" role. Finish creating the service account.

After the service account has been created, click on it from the list of "Service Accounts" for your project. Then, visit the "Keys" tab to create new JSON credentials file. This will trigger your browser to download a JSON file into your Downloads folder. Finally, move the downloaded JSON file into the root directory of this repository, and rename it to "google-credentials.json" specifically.
