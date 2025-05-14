# Demo

## Backend Setup

    cd <root>/backend
    brew install python@3.13

### Pipenv

    brew install pipenv
    pipenv shell
    <!-- TODO: see if this is still necessary pipenv install --python 3.13 -->
    pipenv sync --python 3.13


### Database Setup
#### Installation
    brew uninstall postgresql
    brew install postgresql@16

The following commands are from the output of installing postgres 16, so they may differ in your terminal. This puts postgres on the path.

    echo 'export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"' >> ~/.zshrc
    export LDFLAGS="-L/opt/homebrew/opt/postgresql@16/lib"
    export CPPFLAGS="-I/opt/homebrew/opt/postgresql@16/include"
    export PKG_CONFIG_PATH="/opt/homebrew/opt/postgresql@16/lib/pkgconfig"

The postgres 16 installation output also suggests starting the service, but it may have already started:

    brew services start postgresql@16

#### Creating DB
Access psql with the following command:

    sudo psql -U postgres

If the above command fails, you may need to (separately install the psql command)[https://stackoverflow.com/questions/44654216/correct-way-to-install-psql-without-full-postgres-on-macos#answer-55564878].

Then, set up the database and user:

    CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'postgres';
    CREATE DATABASE demo;
    grant all privileges on database demo to postgres;
    \q

Also, add an environment variable for your database connection. If you used the same values as suggested above, run the following to set the local url:

    export DB_URI=postgresql://postgres:postgres@localhost:5432/demo
    export FLASK_APP=app/app.py <!-- TODO: see if this export is necessary. This env var is in the .env file. -->


#### Migrations
Make sure the `migrations/versions` directory is present. If not, in the root of the project, run

    flask db init


Then, run the migrations with the following script:

    flask db upgrade


To generate a db migration, first update a model class and then run

    flask db migrate -m "Edit this migration message."


And to downgrade,

    flask db downgrade

Remember to DROP any ENUMs you have by manually adding this to the migrations versions file under downgrade(), eg.:

    sa.Enum(name='ink_format').drop(op.get_bind())

Note that upgrading or downgrading may drop columns or tables, so be sure that the migration content is what you want it to be before running these two commands. You can find the migration file in migrations/versions, and its name will be output after running migrate.


## Run
Run the following from the project's backend directory (`cd backend` from root):

    flask run --debug

## Frontend Setup
Run the following:

    cd <root>/frontend
    yarn dev
# flask_next_js_template
