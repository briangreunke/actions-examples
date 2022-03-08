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
- Only allow merge from `staging` (right now a manual process)

### Staging
- Require a pull request before merging to `staging`
- Also require for admins

# Feature update
- Create new branch
- update, commit, push
- run unit and integration tests
- merge to `staging`
- merge `staging` to `master`

# Deploy to production workflow
- if branch is main
    - validate secrets exist
    - validate infrastructure
    - deploy to prod

# Deploy to staging workflow
- if branch is staging
    - validate secrets exist
    - validate infrastructure
    - deploy to staging
