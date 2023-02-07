# Translation workflow

Translations in this directory are managed by Smartling.
Do not manually edit any files except in the en-US directory.

## Steps to get translations

1. Add/update strings in en-US.
2. Open to the ['Files' tab for the Recommendation API project in Smartling](https://dashboard.smartling.com/app/projects/8152f9b61/files/list.html).
3. Drag-and-drop files from the en-US directory to Smartling to upload them.
4. Select all files on Smartling and click 'Request Translation'. Follow the prompts to create a new job.
5. Authorize the newly created job for translation.
6. Wait until translations are completed.
7. Select all files in the ['Files' tab for the Recommendation API project in Smartling](https://dashboard.smartling.com/app/projects/8152f9b61/files/list.html) and click 'Download selected' located in the menu icon.
8. Replace files in this repo with the downloaded translation files. Commit and merge as usual.

## Potential workflow improvements

### Automatically download translations
The last 3 steps in the above workflow can be avoided by 
automatically pulling in translation files using the 
[Smartling REST API](https://api-reference.smartling.com/) or the 
[Smartling Python SDK](https://pypi.org/project/SmartlingApiSdk/).

### Shared translation files
If translation files should be shared between multiple repos, consider creating a dedicated repo for translations.
Translations can then be pulled in using the Smartling API, or by exporting a Python library, similar to
[Pocket/web-localization](https://github.com/Pocket/web-localization/).
