ALTER TABLE Clientes
ADD CONSTRAINT chk_clientes_email
CHECK (
    Email IS NULL
    OR Email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
);