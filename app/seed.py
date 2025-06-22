import csv
from app import create_app, db
from app.models import Guest, Episode

# Initialize the app context
app = create_app()
app.app_context().push()

# Drop and recreate all tables
db.drop_all()
db.create_all()

print("🌱 Seeding database...")

# Load guests from guests.csv
try:
    with open('guests.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest = Guest(name=row['name'], occupation=row['occupation'])
            db.session.add(guest)
except FileNotFoundError:
    print("❌ 'guests.csv' not found! Make sure it's in the root of your project.")
    exit()

# Manually add some episodes
episode1 = Episode(date="1/11/99", number=1)
episode2 = Episode(date="1/12/99", number=2)
db.session.add_all([episode1, episode2])

# Commit everything
db.session.commit()
print("✅ Done seeding!")
