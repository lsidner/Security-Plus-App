# Security+ Study App

A desktop application to help you study for the CompTIA Security+ exam. Features flashcards with simplified spaced repetition, a question bank, PBQ support, quizzes, progress tracking, and import/export functionality. The database is created and stored locally in the user's home directory.

## Installation

1. **Requirements**: Python 3.8+, [PySide6](https://pypi.org/project/PySide6/), [matplotlib](https://pypi.org/project/matplotlib/) (optional for charts).
2. **Install dependencies**:
   ```sh
   pip install PySide6 matplotlib
   ```
3. **Clone or download this repository**.

## Usage

Run the app from your terminal:
```sh
python security_app.py
```

### Importing Questions

- **CSV**: Use a header row with columns: `domain,question,answer,type`.
- **JSON**: Each item should include `domain`, `question`, `answer`, and `type`.

### Exporting Questions

- Go to the **Settings** tab and click "Export Question Bank (JSON)".

### Resetting Progress

- Go to the **Settings** tab and click "Reset Database" to delete all questions and progress.

## Contributing

Pull requests and suggestions are welcome! Please open an issue for bugs or feature requests.

## License

MIT License. See [LICENSE](LICENSE) for details.