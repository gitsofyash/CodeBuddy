# CodeBuddy Repository Details

Use these details to make the GitHub repository look complete and professional.

## About

Description:

```text
Free push-notification automation that sends daily, random, and progress-based LeetCode practice questions using Python.
```

Website:

```text
https://github.com/gitsofyash/CodeBuddy
```

Topics:

```text
python
leetcode
ntfy
push-notifications
github-actions
automation
coding-practice
free
```

## Social Preview

Suggested preview text:

```text
CodeBuddy sends free daily LeetCode practice notifications with problem links, solution links, and discussion links.
```

Suggested screenshot idea:

```text
A phone or browser screenshot showing a CodeBuddy ntfy notification with the problem link and solution link.
```

## GitHub Actions

Workflow file:

```text
.github/workflows/codebuddy.yml
```

Required repository secret:

```text
NTFY_TOPIC
```

Optional repository variable:

```text
NTFY_SERVER=https://ntfy.sh
```

Default schedule:

```text
10:00 AM IST daily
```

Cron:

```text
30 4 * * *
```

For 12:00 PM IST:

```text
30 6 * * *
```

## Recommended Settings

- Enable Issues.
- Enable Actions.
- Keep `NTFY_TOPIC` as a secret.
- Add a license.
- Add a social preview image when available.
- Protect `master` if you plan to accept contributions.

## Suggested Pinned Repo Description

```text
Python automation for free daily LeetCode push notifications via ntfy and GitHub Actions.
```
