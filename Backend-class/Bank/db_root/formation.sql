CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50),
  password_hash VARCHAR(255),
  full_name VARCHAR(100),
  role VARCHAR(20),
  is_active BOOLEAN,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS borrowers (
  id SERIAL PRIMARY KEY,
  national_code VARCHAR(10),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  father_name VARCHAR(50),
  birth_date DATE,
  phone VARCHAR(15),
  mobile VARCHAR(15),
  address TEXT,
  postal_code VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS loans (
  id SERIAL PRIMARY KEY,
  borrower_id INT REFERENCES borrowers(id),
  loan_amount DECIMAL(15,2),
  installment_count INTEGER,
  start_date DATE,
  end_date DATE,
  loan_type VARCHAR(50),
  status VARCHAR(20),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS installments (
  id SERIAL PRIMARY KEY,
  loan_id INTEGER REFERENCES loans(id),
  installment_number INTEGER,
  due_date DATE,
  amount DECIMAL(15, 2),
  paid_amount DECIMAL(15, 2),
  status VARCHAR(20),
  paid_date DATE,
  delays_date INTEGER
);

CREATE TABLE IF NOT EXISTS payments (
  id SERIAL PRIMARY KEY,
  installment_id INTEGER REFERENCES installments(id),
  amount DECIMAL(15, 2),
  payment_date DATE,
  payment_method VARCHAR(50),
  reference_number VARCHAR(100),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS guarantors (
  id SERIAL PRIMARY KEY,
  loan_id INTEGER REFERENCES loans(id),
  national_code VARCHAR(10),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone VARCHAR(15),
  address TEXT,
  relationship VARCHAR(50)
);
