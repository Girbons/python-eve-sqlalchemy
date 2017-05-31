from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from tables import Base, People

app = Eve(validator=ValidatorSQL, data=SQL)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

# Insert some example data in the db
if not db.session.query(People).count():
    import example_data
    for item in example_data.test_data:
        db.session.add(People.from_tuple(item))
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
