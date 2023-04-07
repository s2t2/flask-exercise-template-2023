

# Google Login Setup

## Consent Screen

Visit the [Consent Screen](https://console.cloud.google.com/apis/credentials/consent) page for your Google Cloud project.

Click to "Configure Consent Screen". Leave the domain info blank, and leave the defaults / skip lots of the setup for now.

If/when you deploy your app to a production server, you can return to populating this info (or you will be using a different project).

## Google OAuth Client

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page for your Google Cloud project.

Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id".

Choose a "Web application" type, give it a name. Set the following "Authorized Redirect URIs":

  + http://localhost:5000/auth/google/callback

After the client is created, note the `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`, and set them as environment variables in the ".env" file.


## Troubleshooting Notes

### Profile Image

After logging in with Google sometimes a broken profile image would be displayed.

References:
  + https://support.mozilla.org/en-US/questions/1274574
  + https://apple.stackexchange.com/questions/345500/problem-loading-images-from-googleusercontent
  + https://support.google.com/mail/thread/22286413/google-images-from-lh3-googleusercontent-com-not-showing?hl=en


Adding a "no-referrer" to the Boostrap 5 Layout seems to fix it:

  + https://stackoverflow.com/questions/56242788/http-403-on-images-loaded-from-googleusercontent-com
  + https://mazeez.dev/posts/why-google-oauth-profile-picture-returns-403
