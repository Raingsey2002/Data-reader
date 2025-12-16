
CREATE TYPE level_enum AS ENUM ('National Level', 'Sub-National Level', 'APE');
CREATE TYPE kind_enum AS ENUM ('Report', 'Query');

CREATE TABLE IF NOT EXISTS rows (
    id SERIAL PRIMARY KEY,
    rq TEXT NOT NULL,
    name TEXT NOT NULL,
    "desc" TEXT NOT NULL,
    count TEXT NOT NULL,
    "user" TEXT NOT NULL,
    level level_enum NOT NULL,
    entity TEXT NOT NULL,
    office TEXT NOT NULL,
    ou TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    type kind_enum NOT NULL,
    code TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_rows_level ON rows (level);
CREATE INDEX IF NOT EXISTS idx_rows_entity ON rows (entity);
CREATE INDEX IF NOT EXISTS idx_rows_year ON rows (year);
CREATE INDEX IF NOT EXISTS idx_rows_month ON rows (month);
CREATE INDEX IF NOT EXISTS idx_rows_type ON rows (type);
CREATE INDEX IF NOT EXISTS idx_rows_code ON rows (code);
