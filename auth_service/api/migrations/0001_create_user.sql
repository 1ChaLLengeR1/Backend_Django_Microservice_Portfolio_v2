CREATE TABLE IF NOT EXISTS user (
    id TEXT PRIMARY KEY NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    last_login DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);



INSERT INTO user (id, login, password, last_login, created_at)
VALUES
    ('70f3ddb6-9446-442f-a407-0a057bbb02aa', 'ChaLLengeR', '$2a$10$DLqeI0sHfRCP5L.UnNLRsObjJepM4FY2f8bRs12TOrF4xCzMmEJQq', NULL, CURRENT_TIMESTAMP),
    ('9bd49bdd-38cc-4f0b-aeb0-5dccea07d222', 'Guest', '$2a$10$LFaeRIszVvlTPPWi7GNQJuaSO3a93DIR0prLOOe/XRIrLxWBC2aHO', NULL, CURRENT_TIMESTAMP);


