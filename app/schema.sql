CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TABLE bookings (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    room text NOT NULL,
    period tstzrange NOT NULL,
    EXCLUDE USING gist (room WITH =, period WITH &&)
);
