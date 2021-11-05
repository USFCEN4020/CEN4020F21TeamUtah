CREATE TABLE IF NOT EXISTS Username(
    username TEXT PRIMARY KEY,
    password TEXT,
    firstname TEXT,
    lastname TEXT,
    logedIn NOT NULL CHECK (logedIn IN (0, 1)) DEFAULT 0,
    email BOOLEAN NOT NULL CHECK (email IN (0, 1)) DEFAULT 1,
    sms BOOLEAN NOT NULL CHECK (sms IN (0, 1)) DEFAULT 1,
    marketing BOOLEAN NOT NULL CHECK (marketing IN (0, 1)) DEFAULT 1,
    isPlus BOOLEAN NOT NULL CHECK (isPlus IN (0, 1)) DEFAULT 0,
    language TEXT DEFAULT 'english',
    applnumber INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS Profile(
    username TEXT PRIMARY KEY,
    title TEXT,
    major TEXT,
    universityName TEXT,
    about TEXT
);
CREATE TABLE IF NOT EXISTS Experience(
    username TEXT,
    title TEXT,
    employer TEXT,
    startDate TEXT,
    endDate TEXT,
    location TEXT,
    description TEXT
);
CREATE TABLE IF NOT EXISTS Education(
    username TEXT,
    schoolName TEXT,
    degree TEXT,
    yearsAttended INTEGER
);
CREATE TABLE IF NOT EXISTS Messages(
    sender TEXT,
    receiver TEXT,
    content TEXT,
    timestamp INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INT)) NOT NULL,
    isRead BOOLEAN NOT NULL CHECK (isRead IN (0, 1)) DEFAULT 0
);
CREATE TABLE IF NOT EXISTS DeletedMessages(user TEXT, messageId INTEGER);
CREATE TABLE IF NOT EXISTS Experience(
    username TEXT,
    title TEXT,
    employer TEXT,
    startDate TEXT,
    endDate TEXT,
    location TEXT,
    description TEXT
);
CREATE TABLE IF NOT EXISTS Education(
    username TEXT,
    schoolName TEXT,
    degree TEXT,
    yearsAttended INTEGER
);
CREATE TABLE IF NOT EXISTS Friends(
    userOne TEXT,
    userRequested TEXT,
    request INTEGER
);
CREATE TABLE IF NOT EXISTS Jobs(
    jobid INT,
    username TEXT,
    title TEXT,
    description TEXT,
    employer TEXT,
    location TEXT,
    salary REAL
);
CREATE TABLE IF NOT EXISTS Applications(
    jobid INT,
    username TEXT,
    title TEXT,
    grad_date TEXT,
    entry_date TEXT,
    description TEXT,
    timestamp INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INT)) NOT NULL
);
CREATE TABLE IF NOT EXISTS Seenjobs(
    jobid INT,
    username TEXT
);
CREATE TABLE IF NOT EXISTS Seenprofiles(
    username TEXT,
    profilename TEXT
);
