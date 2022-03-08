# Set up
## Environments
Define different Github environments
- Testing: `test`
- Staging: `staging`
    - Also set `fail` as a "Deployment branch" to demonstrate a failed secret
- Production: `prod`

## Secrets
Secrets are stored per environment
- Testing: `TEST_SECRET`
- Staging: `STAGING_SECRET`
- Production: `PROD_SECRET`

## Controls
### Main
- Require a pull request before merging to `main`
- Only allow merge from `staging`

### Staging
- Require a pull request before merging to `staging`
- Require review in the above pull requests
- Also require for admins


# Deploy to production workflow
- if branch is main
    - deploy to prod

# Deploy to staging workflow
- if branch is staging
    - deploy to staging

# TODO:
- How to trigger on merge to master?