CREATE DATABASE microuser;
CREATE DATABASE microtrip;
CREATE DATABASE micropayment;
CREATE DATABASE microdispatch;


CREATE USER microuser_user WITH ENCRYPTED PASSWORD 'password';
CREATE USER microtrip_user WITH ENCRYPTED PASSWORD 'password';
CREATE USER micropayment_user WITH ENCRYPTED PASSWORD 'password';
CREATE USER microdispatch_user WITH ENCRYPTED PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE microuser TO microuser_user;
GRANT ALL PRIVILEGES ON DATABASE microtrip TO microtrip_user;
GRANT ALL PRIVILEGES ON DATABASE micropayment TO micropayment_user;
GRANT ALL PRIVILEGES ON DATABASE microdispatch TO microdispatch_user;