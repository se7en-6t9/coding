#!/usr/bin/env python3
"""
GitHub Account Status Checker

This script checks if a GitHub account has Pro features.
Usage: python check_github_status.py <username> [github_token]

Note: GitHub API has rate limits. For best results, provide a GitHub personal access token.
"""

import sys
import json
try:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError
except ImportError:
    print("Error: This script requires Python 3")
    sys.exit(1)


def check_github_pro_status(username, token=None):
    """
    Check if a GitHub user has Pro features.
    
    Args:
        username (str): GitHub username to check
        token (str, optional): GitHub personal access token for authentication
        
    Returns:
        dict: User information including account type
    """
    api_url = f"https://api.github.com/users/{username}"
    
    try:
        # Create request with a user agent (required by GitHub API)
        req = Request(api_url)
        req.add_header('User-Agent', 'GitHub-Status-Checker')
        
        # Add authentication if token is provided
        if token:
            req.add_header('Authorization', f'token {token}')
        
        with urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        # Extract relevant information
        user_info = {
            'username': data.get('login'),
            'name': data.get('name'),
            'account_type': data.get('type'),
            'plan': data.get('plan', {}).get('name', 'Not visible') if data.get('plan') else 'Not visible',
            'public_repos': data.get('public_repos'),
            'followers': data.get('followers'),
            'created_at': data.get('created_at'),
        }
        
        return user_info
        
    except HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found")
        elif e.code == 403:
            print(f"Error: Rate limit exceeded or access forbidden.")
            print("Try providing a GitHub personal access token as the second argument.")
            print("Create one at: https://github.com/settings/tokens")
        else:
            print(f"HTTP Error {e.code}: {e.reason}")
        return None
    except URLError as e:
        print(f"Network Error: {e.reason}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def print_manual_instructions():
    """Print instructions for manually checking GitHub Pro status."""
    print("\n" + "=" * 70)
    print("HOW TO CHECK IF YOU'RE USING GITHUB PRO (Manual Method)")
    print("=" * 70)
    print("\n1. Go to https://github.com/settings/billing")
    print("2. Look at your current plan")
    print("3. GitHub Pro features include:")
    print("   - Advanced code review tools")
    print("   - 3,000 GitHub Actions minutes/month")
    print("   - 2GB of GitHub Packages storage")
    print("   - GitHub Copilot (with separate subscription)")
    print("   - Protected branches on private repos")
    print("   - Multiple assignees and reviewers")
    print("   - Wiki pages for private repos")
    print("\n4. If you see 'GitHub Pro' or 'Pro' in your billing settings, you have it!")
    print("=" * 70 + "\n")


def main():
    if len(sys.argv) < 2:
        print("=" * 70)
        print("GitHub Pro Status Checker")
        print("=" * 70)
        print("\nUsage: python check_github_status.py <username> [github_token]")
        print("\nExamples:")
        print("  python check_github_status.py octocat")
        print("  python check_github_status.py yourname ghp_yourTokenHere")
        print_manual_instructions()
        sys.exit(1)
    
    username = sys.argv[1]
    token = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"Checking GitHub account status for: {username}\n")
    
    user_info = check_github_pro_status(username, token)
    
    if user_info:
        print("=" * 70)
        print(f"Username: {user_info['username']}")
        if user_info['name']:
            print(f"Name: {user_info['name']}")
        print(f"Account Type: {user_info['account_type']}")
        print(f"Plan: {user_info['plan']}")
        print(f"Public Repositories: {user_info['public_repos']}")
        print(f"Followers: {user_info['followers']}")
        print(f"Account Created: {user_info['created_at']}")
        print("=" * 70)
        
        # Determine if it's a Pro account
        plan_name = user_info['plan'].lower()
        if 'pro' in plan_name:
            print("\n✓ This account has GitHub Pro features!")
        elif plan_name == 'free':
            print("\n✗ This account is using the Free plan.")
        elif plan_name == 'not visible':
            print("\n? Plan information not available via API.")
            print("  Note: Plan details are only visible for authenticated requests")
            print("  with proper permissions, or for your own account.")
        else:
            print(f"\n? Account plan: {user_info['plan']}")
        
        print_manual_instructions()
    else:
        print("\nAPI check failed. See manual instructions below:")
        print_manual_instructions()
        sys.exit(1)


if __name__ == "__main__":
    main()
