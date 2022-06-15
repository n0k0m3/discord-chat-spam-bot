# Discord chat spam bot
- Use `secret.json` to configure the bot MFA Auth key and channel to spam in.
- Use `cronjob` in workflow to automate spamming

## How to use
Client side:
- Get `git-crypt` working: https://buddy.works/guides/git-crypt and run `git-crypt init`
- By default, `.gitattributes` already has an entry to encrypt `discord_farming/secret.json`

Github side:
- We use Github Action `git-crypt` to unlock: https://github.com/marketplace/actions/github-action-to-unlock-git-crypt-secrets
- Base64 key generate: `git-crypt export-key ./tmp-key && cat ./tmp-key | base64`
- Add the base64 key to `GIT_CRYPT_KEY` in Settings > Secrets > Actions (Actions secrets)