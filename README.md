# Set up
- Secrets are stored by branch


# Controls
- no push to main, only merge
- no push to staging, only merge
- require review for the above

# Deploy to production workflow
- if branch is main
    - deploy to prod

# Deploy to staging workflow
- if branch is staging
    - deploy to staging

# Create a branch
