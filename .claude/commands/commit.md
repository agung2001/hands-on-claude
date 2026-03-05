Guide the user through a clean git commit following this project's git-workflow rules.

## Steps

1. Run `git status` to show what has changed.
2. Run `git diff` (unstaged) and `git diff --cached` (staged) so both you and the user can see what will be committed.
3. Ask the user which files to stage (never use `git add .` blindly).
4. Stage only the specified files.
5. Run `git diff --staged` and show the user a summary of what is staged.
6. Propose a commit message in Conventional Commits format:
   ```
   <type>(<scope>): <short summary>
   ```
   Choose the type from: `feat`, `fix`, `style`, `refactor`, `docs`, `chore`.
   The scope is the experiment name or area (e.g. `landing-page`, `particle-clock`, `rules`).
7. Ask the user to confirm or edit the message before committing.
8. Only run `git commit` after the user explicitly approves the message.
9. Do NOT push — remind the user to confirm before any `git push`.
