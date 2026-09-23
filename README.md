# Branching & Feature Development — Oops Git Project

A beginner-friendly Python project that demonstrates **Git branching, feature development, and merging** workflows using a small "Learning Platform" application.

- **Repository:** https://github.com/rajgenai4u/Branching_Feature_Development_oops_git_project
- **Author:** Karre Rajesh (rajgenai4u@gmail.com)
- **Date of operations:** 23 September 2026
- **Working directory:** `Branching_and_Feature_Development/`

---

## Project Structure

```
Branching_and_Feature_Development/
├── README.md       # This file — project documentation
├── login.py        # Login feature (from feature-login branch)
├── dashboard.py    # Role-based dashboard feature (from feature-dashboard branch)
└── profile.py      # Profile feature placeholder (from feature-profile branch)
```

---

## Files & What They Do

### `login.py` (7 lines)
Simple credential-check function.

```python
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful!"
    return "Invalid credentials."

if __name__ == "__main__":
    print(login("admin", "1234"))
```

Run it:
```bash
python login.py
# Output: Login successful!
```

### `dashboard.py` (9 lines)
Role-based dashboard message renderer.

```python
def display_dashboard(role):
    if role == "Student":
        return "Welcome to Student Dashboard: View enrolled courses."
    elif role == "Mentor":
        return "Welcome to Mentor Dashboard: View assigned mentees."
    return "Welcome to General Dashboard."

if __name__ == "__main__":
    print(display_dashboard("Student"))
```

Run it:
```bash
python dashboard.py
# Output: Welcome to Student Dashboard: View enrolled courses.
```

### `profile.py` (0 lines)
Empty placeholder file created on the `feature-profile` branch (ready for future profile logic).

---

## Branches

| Branch | Remote Tracking | Status |
|---|---|---|
| `main` | `origin/main` | Up to date, all features merged ✅ |
| `feature-login` | `origin/feature-login` | Merged into `main` (fast-forward) ✅ |
| `feature-profile` | `origin/feature-profile` | Merged into `main` ✅ |
| `feature-dashboard` | `origin/feature-dashboard` | Merged into `main` ✅ |

Current branch: **`main`** — working tree clean.

---

## Commit History (all on 23 Sep 2026)

```
*   cd1bd1e (HEAD -> main, origin/main) Mearge feature-dashboard into main
|\
| * db82ffb (origin/feature-dashboard, feature-dashboard) added rolebased dashoard to file
| * eb6523a Added role based to dashboard
* |   ddcf284 Mearge feature-profile into main
|\ \
| * | 80757ff (origin/feature-profile, feature-profile) added profile file in feature-profile branch
| |/
* | 66b8b59 (origin/feature-login, feature-login) Added login.py in feature-login
* | 5448098 created login.py in feature-login branch
|/
* 76c4aee Intial commit on main
```

### Commit Details

| Hash | Branch | Message | Change |
|---|---|---|---|
| `76c4aee` | main | Intial commit on main | Created `README.md` (1 line) |
| `5448098` | feature-login | created login.py in feature-login branch | Created empty `login.py` |
| `66b8b59` | feature-login | Added login.py in feature-login | Added login function (7 lines) |
| `80757ff` | feature-profile | added profile file in feature-profile branch | Created empty `profile.py` |
| `eb6523a` | feature-dashboard | Added role based to dashboard | Created empty `dashboard.py` |
| `db82ffb` | feature-dashboard | added rolebased dashoard to file | Added role-based dashboard (9 lines) |
| `ddcf284` | main (merge) | Mearge feature-profile into main | Merge commit: parents `66b8b59` + `80757ff` (ort strategy) |
| `cd1bd1e` | main (merge) | Mearge feature-dashboard into main | Merge commit: parents `ddcf284` + `db82ffb` (ort strategy) |

> **Note:** The `feature-login` merge into `main` was a **fast-forward** (no merge commit created, `-m` option ignored), because `main` had no new commits since branching.

---

## Git Commands Performed

### 1. Initialize repository & first commit (on `main`)
```bash
git init
echo "# Learning Platform Project" > README.md
git add README.md
git commit -m "Intial commit on main"
```

### 2. Setup remote & push
```bash
git remote add origin git@github.com:rajgenai4u/Branching_Feature_Development_oops_git_project.git
git push -u origin main
```

### 3. Login feature (`feature-login`)
```bash
git checkout main
git checkout -b feature-login

# Create empty file and commit
touch login.py
git add login.py
git commit -m "created login.py in feature-login branch"

# Add the login function and commit
# (edit login.py)
git add login.py
git commit -m "Added login.py in feature-login"

# Merge into main (fast-forward)
git checkout main
git merge feature-login
git push origin feature-login
```

### 4. Profile feature (`feature-profile`)
```bash
git checkout main
git checkout -b feature-profile

touch profile.py
git add profile.py
git commit -m "added profile file in feature-profile branch"

# Merge into main (created merge commit)
git checkout main
git merge feature-profile -m "Mearge feature-profile into main"
git push origin feature-profile
```

### 5. Dashboard feature (`feature-dashboard`)
```bash
git checkout main
git checkout -b feature-dashboard

touch dashboard.py
git add dashboard.py
git commit -m "Added role based to dashboard"

# Add role-based logic and commit
# (edit dashboard.py)
git add dashboard.py
git commit -m "added rolebased dashoard to file"

# Merge into main (created merge commit)
git checkout main
git merge feature-dashboard -m "Mearge feature-dashboard into main"
git push origin feature-dashboard
```

### 6. Final push of merged `main`
```bash
git push origin main
```

### 7. Inspection commands used along the way
```bash
git status                 # check working tree
git status -sb             # short status with branch tracking
git branch                 # list local branches
git branch -a              # list local + remote branches
git log --oneline --all    # compact history of all branches
git log --graph --oneline --all --decorate   # visual branch/merge graph
git log --pretty=format:"%h %an %ad %s" --date=short   # detailed log
git remote -v              # show remote URLs
git reflog                 # history of HEAD movements (checkouts, commits, merges)
git show <commit>          # inspect a specific commit's diff
git ls-tree -r main --name-only   # list files tracked on main
```

---

## Workflow Summary

1. **Initial commit** on `main` with `README.md`.
2. Created **three feature branches** from `main`: `feature-login`, `feature-profile`, `feature-dashboard`.
3. Developed each feature **independently** on its own branch (2 commits each for login & dashboard, 1 for profile).
4. **Merged each branch back into `main`:**
   - `feature-login` → fast-forward merge
   - `feature-profile` → merge commit `ddcf284`
   - `feature-dashboard` → merge commit `cd1bd1e`
5. **Pushed** all branches and the updated `main` to GitHub.

```
main ──●──────────────●─────●─────●  (cd1bd1e) final
        \            /      |     /
feature-login ──●───●       |     |
                       \    |     |
feature-profile ────────●───|─────|
                                  |
feature-dashboard ──●──●──────────┘
```

---

## Current State

- Branch: `main`, up to date with `origin/main`
- Working tree: **clean** (nothing to commit)
- All 3 feature branches merged and pushed ✅
- 8 commits total across all branches
