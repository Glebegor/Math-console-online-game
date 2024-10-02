CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE statistic (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    count_of_wins INTEGER NOT NULL,
    count_of_loses INTEGER NOT NULL,
    count_of_games INTEGER NOT NULL,
    biggest_number INTEGER NOT NULL,
    win_streak INTEGER NOT NULL,
    bigger_win_streak INTEGER NOT NULL,
    
    FOREIGN KEY (user_id) REFERENCES users (id)
)