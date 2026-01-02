# coding

## GitHub Pro Status Checker

A simple utility to check if a GitHub account has Pro features.

### Quick Answer: "Am I using GitHub Pro?"

**Option 1 - Check Manually (Recommended):**
1. Go to [https://github.com/settings/billing](https://github.com/settings/billing)
2. Look at your current plan
3. If it says "GitHub Pro" or "Pro", you have it!

**Option 2 - Use this script:**

```bash
python check_github_status.py <username> [github_token]
```

### Usage Examples

```bash
# Without authentication (limited by API rate limits)
python check_github_status.py your-username

# With authentication (recommended, no rate limits)
python check_github_status.py your-username ghp_yourPersonalAccessToken

# Show usage and manual instructions
python check_github_status.py
```

### What GitHub Pro Includes

- Advanced code review tools
- 3,000 GitHub Actions minutes/month
- 2GB of GitHub Packages storage
- Protected branches on private repositories
- Multiple assignees and reviewers
- Wiki pages for private repositories
- Pages and GitHub Insights

### Requirements

- Python 3.x (uses standard library only, no additional dependencies)

### Creating a GitHub Personal Access Token

If you need to use the API method:
1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name and select the `read:user` scope
4. Click "Generate token" and copy it
5. Use it with the script: `python check_github_status.py your-username ghp_token`

### Note

The GitHub API does not always expose plan information for public queries. For the most accurate result, check your billing settings directly or use an authenticated API request with your own token.