CREATE TABLE IF NOT EXISTS movie
(
    id    VARCHAR(12)   NOT NULL PRIMARY KEY,
    title text          NOT NULL,
    year  VARCHAR(12)    NOT NULL,
    rate  NUMERIC(5, 2) NOT NULL DEFAULT 0.0
);
COMMENT ON COLUMN movie.id IS 'Unique movie imdb ID';
COMMENT ON COLUMN movie.title IS 'The movie commercial name';
COMMENT ON COLUMN movie.rate IS 'The movie qualification between 0 and 100';
