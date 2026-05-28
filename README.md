# Security+ Study App

A desktop application to help you study for the CompTIA Security+ exam. It includes flashcards with spaced repetition, question imports, an inline quiz workflow, per-attempt results, and quiz history tracking. The database is created and stored locally in the user's home directory (C:\Users\username\.security_plus_study_app).

## Features

- **Flashcards** with simplified spaced repetition and review scheduling.
- **Question bank import** from CSV and JSON files.
- **Inline quiz mode** in the Quiz tab, including multiple-choice buttons.
- **Quiz results** after each attempt, including which answers were wrong and explanations.
- **Quiz history** with per-attempt details, including explanations for each question.
- **Progress tracking** and local database storage.

## Installation

1. **Requirements**: Python 3.8+, [PySide6](https://pypi.org/project/PySide6/), and optional plotting dependencies if you use charting features.
2. **Install dependencies**:
   ```sh
   pip install PySide6
   ```
3. **Clone or download this repository**.
   ```sh
   git clone https://github.com/lnsydnr/Security-Plus-App
   ```

## Usage

Run the app from your terminal:
```sh
python security_app.py
```

### Quiz workflow

- Open the **Quiz** tab to choose a domain and question count.
- Answer questions inline. Multiple-choice questions show selectable options directly in the quiz tab.
- After the quiz finishes, review the results table for correct/incorrect answers and explanations.
- Open the **History** tab to view prior quiz attempts and detailed answer breakdowns.

### Importing Questions

- **CSV**: Use a header row with columns: `domain,question,answer,type`.
- **JSON**: Each item can include `domain`, `question`, `answer`, `type`, `options`, and `explanation`.

Example JSON item:
```json
{
  "question": "Which protocol is used to securely transfer files over a network?",
  "domain": "Network Security",
  "options": ["FTP", "SFTP", "Telnet", "SMTP"],
  "answer": "SFTP",
  "explanation": "SFTP uses SSH to securely transfer files."
}
```

### Exporting Questions

- Go to the **Settings** tab and click "Export Question Bank (JSON)".

### Resetting Progress

- Go to the **Settings** tab and click "Reset Database" to delete all questions and progress.

## Contributing

Pull requests and suggestions are welcome! Please open an issue for bugs or feature requests.

## License

MIT License. See [LICENSE](LICENSE) for details.