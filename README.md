# CodeBuddy

CodeBuddy is a free Python automation that sends LeetCode practice prompts as push notifications with ntfy. It can send a random problem, the official daily challenge, and a difficulty-based problem that gets harder as your solved-question count increases.

## Features

- Sends LeetCode questions as free push notifications.
- Supports random, daily, and progress-based difficulty questions.
- Includes free LeetCode solution and discussion links for step-by-step study.
- Tracks difficulty progression locally in `questions_completed.json`.
- Uses ntfy with `.env` configuration. No bot or account required.
- Runs locally or automatically with GitHub Actions.
- Includes a Windows-friendly `script.bat` for Task Scheduler.

## Tech Stack

- Python
- Requests
- python-dotenv
- ntfy
- LeetCode public problem API and GraphQL daily challenge endpoint

## Project Structure

```text
CodeBuddy/
|-- main.py
|-- requirements.txt
|-- script.bat
|-- .env.example
|-- CHANGELOG.md
|-- LICENSE
|-- .github/
|   |-- workflows/
|   |   `-- codebuddy.yml
|   |-- ISSUE_TEMPLATE/
|   `-- pull_request_template.md
|-- questions/
|   |-- daily_question.py
|   |-- difficulty_question.py
|   |-- leetcode_api.py
|   `-- random_question.py
`-- utils/
    |-- data_storage.py
    `-- send_message.py
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- The free ntfy mobile app, or a browser tab open to your ntfy topic

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/gitsofyash/CodeBuddy.git
cd CodeBuddy
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create your local environment file:

```bash
copy .env.example .env
```

Update `.env` with your ntfy topic:

```env
NTFY_TOPIC=codebuddy-your-unique-topic
NTFY_SERVER=https://ntfy.sh
```

Choose a topic name that is hard for others to guess, for example `codebuddy-yash-2026-strong-random-word`.

To receive notifications:

1. Install the ntfy app from <https://ntfy.sh/app>.
2. Subscribe to the same topic you put in `NTFY_TOPIC`.
3. Or open `https://ntfy.sh/your-topic-name` in a browser.

## Usage

Run the app manually:

```bash
python main.py
```

By default, CodeBuddy sends:

1. A random LeetCode question.
2. A difficulty-based question.
3. The official daily LeetCode challenge.

The difficulty-based message starts at Easy, switches to Medium after 15 tracked sends, and switches to Hard after 70 tracked sends.

Each notification includes:

- The problem link.
- Acceptance rate.
- LeetCode solutions link.
- LeetCode discussion link.
- A short study flow reminder.

Send only one type of question:

```bash
python main.py --type daily
python main.py --type random
python main.py --type difficulty
```

## Automating On Windows

Use Windows Task Scheduler to run `script.bat` daily:

1. Open Task Scheduler.
2. Choose **Create Basic Task**.
3. Pick a daily trigger and set the time, such as 10:00 AM or 12:00 PM.
4. Select **Start a Program**.
5. Browse to this repository's `script.bat`.

The batch file automatically changes into the project directory before running `main.py`.

To send only the daily question at 10:00 AM:

1. Create a daily task for 10:00 AM.
2. Set **Program/script** to your Python executable, for example:

```text
C:\Users\YASH GUPTRA\Documents\CodeBuddy\.venv\Scripts\python.exe
```

3. Set **Add arguments** to:

```text
main.py --type daily
```

4. Set **Start in** to:

```text
C:\Users\YASH GUPTRA\Documents\CodeBuddy
```

For 12:00 PM, create the same task and choose 12:00 PM as the trigger time.

## Automating With GitHub Actions

GitHub Actions can run CodeBuddy every day without keeping your computer on.

### 1. Add Your ntfy Topic As A Secret

In your GitHub repository:

1. Go to **Settings**.
2. Open **Secrets and variables**.
3. Choose **Actions**.
4. Click **New repository secret**.
5. Name it:

```text
NTFY_TOPIC
```

6. Set the value to your ntfy topic, for example:

```text
codebuddy-yash-2026-strong-random-word
```

### 2. Optional: Add ntfy Server As A Variable

The workflow already defaults to `https://ntfy.sh`. If you want to set it manually:

1. Go to **Settings**.
2. Open **Secrets and variables**.
3. Choose **Actions**.
4. Open the **Variables** tab.
5. Add:

```text
NTFY_SERVER=https://ntfy.sh
```

### 3. Choose The Time

The workflow file is at `.github/workflows/codebuddy.yml`.

By default it runs at 10:00 AM IST:

```yaml
- cron: "30 4 * * *"
```

GitHub cron uses UTC. Common India times:

| India time | UTC cron |
| --- | --- |
| 10:00 AM IST | `30 4 * * *` |
| 12:00 PM IST | `30 6 * * *` |

To switch to 12:00 PM IST, change the cron line to:

```yaml
- cron: "30 6 * * *"
```

### 4. Run It Manually

You can test the workflow anytime:

1. Open the **Actions** tab.
2. Select **CodeBuddy Daily Notification**.
3. Click **Run workflow**.
4. Choose `daily`, `random`, `difficulty`, or `all`.

Scheduled workflows send the `daily` question by default.

## How To Study A Question

Use this flow when the notification arrives:

1. Open the problem and spend 20-30 minutes trying it yourself.
2. Write down the brute-force idea first.
3. Look for the bottleneck: repeated work, sorting, extra memory, or slow lookup.
4. Open the solutions link and compare 2-3 approaches.
5. Re-code the cleanest approach without looking.
6. Write a short note with the pattern, time complexity, and the mistake you want to avoid next time.

## Environment Variables

| Variable | Description |
| --- | --- |
| `NTFY_TOPIC` | Topic name where CodeBuddy sends notifications |
| `NTFY_SERVER` | ntfy server URL. Defaults to `https://ntfy.sh` |

## GitHub Repository Settings

Suggested short description:

```text
Free push-notification automation that sends daily, random, and progress-based LeetCode practice questions using Python.
```

Suggested topics:

```text
python, leetcode, ntfy, push-notifications, automation, coding-practice, free
```

Suggested website:

```text
https://github.com/gitsofyash/CodeBuddy
```

Suggested social preview text:

```text
CodeBuddy sends free daily LeetCode practice notifications with problem links, solution links, and discussion links.
```

Recommended GitHub settings:

- Enable **Issues** for bug reports and feature requests.
- Enable **Actions** for the daily scheduler.
- Add `NTFY_TOPIC` as an Actions secret, not a public variable.
- Keep the repository public if you want it to be part of your portfolio.
- Add a screenshot or GIF later showing the notification on phone/browser.

## Roadmap

- Add tests for formatting, difficulty progression, and environment validation.
- Add persistent cloud progress tracking for GitHub Actions difficulty mode.
- Replace local progress tracking with a small database or cloud store.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
