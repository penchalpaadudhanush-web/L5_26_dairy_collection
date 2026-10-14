"""
Dairy Milk Collection Ledger

Records milk deliveries, calculates daily totals, identifies the top
farmer, finds low-fat milk entries, and generates farmer tokens.
"""

import hashlib
import sqlite3


def create_database():
    """Create the in-memory database and its milk collection table."""
    database = sqlite3.connect(":memory:")
    database.execute(
        """
        CREATE TABLE milk (
            id INTEGER PRIMARY KEY,
            farmer TEXT,
            litres REAL,
            fat REAL,
            day TEXT
        )
        """
    )
    return database


def record_milk(db, farmer, litres, fat, day):
    """Record a farmer's milk delivery using a parameterized query."""
    query = (
        "INSERT INTO milk (farmer, litres, fat, day) "
        "VALUES (?, ?, ?, ?)"
    )
    db.execute(query, (farmer, litres, fat, day))
    db.commit()


def farmer_token(farmer):
    """Generate a SHA-256 hash token from a farmer's name."""
    return hashlib.sha256(farmer.encode("utf-8")).hexdigest()


def daily_total(db, day):
    """Calculate the total litres collected on a given day."""
    rows = db.execute(
        "SELECT litres FROM milk WHERE day = ?",
        (day,),
    ).fetchall()
    total = sum(row[0] for row in rows)
    return f"Total: {total:.1f} litres"


def top_farmer(db):
    """Return the farmer with the highest total milk collection."""
    rows = db.execute(
        "SELECT farmer, SUM(litres) "
        "FROM milk GROUP BY farmer"
    ).fetchall()

    if not rows:
        return "No farmer records"

    top = max(rows, key=lambda row: row[1])
    return top[0]


def print_slip(farmer):
    """Display a message indicating that the collection slip is printed."""
    print(f"Printing slip for {farmer}")


def low_fat(db):
    """Find farmers whose milk fat is missing or below 3.5."""
    rows = db.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [
        farmer
        for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run a demonstration of the dairy collection ledger."""
    db = create_database()
    record_milk(db, "Gopal", 12.5, 4.1, "Mon")
    record_milk(db, "Lata", 20.0, 3.2, "Mon")

    print(
        daily_total(db, "Mon"),
        top_farmer(db),
        low_fat(db),
    )
    print_slip("Gopal")
    print(farmer_token("Lata"))
    db.close()


if __name__ == "__main__":
    main()
