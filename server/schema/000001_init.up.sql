CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Use AUTOINCREMENT for SQLite
  username TEXT NOT NULL UNIQUE,  -- Adding UNIQUE constraint to ensure no duplicate usernames
  password TEXT NOT NULL
);

CREATE TABLE statistic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Use AUTOINCREMENT for SQLite
    user_id INTEGER NOT NULL,
    count_of_wins INTEGER NOT NULL DEFAULT 0,
    count_of_loses INTEGER NOT NULL DEFAULT 0,
    count_of_games INTEGER NOT NULL DEFAULT 0,
    biggest_number INTEGER NOT NULL DEFAULT 0,
    win_streak INTEGER NOT NULL DEFAULT 0,
    bigger_win_streak INTEGER NOT NULL DEFAULT 0,
    rating INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE  -- Enforce referential integrity
);
