import sqlite3

DB_PATH = r"c:/Users/PC01/Desktop/HOSPITALFARMACIA/AdminFarmacia/db.sqlite3"

con = sqlite3.connect(DB_PATH)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
rows = [r[0] for r in cur.fetchall()]
keys = [t for t in rows if "descartable" in t.lower() or "dispensa" in t.lower() or "estado" in t.lower()]
print("filtradas", len(keys))
print("\n".join(keys[:200]))

# also show migration tables
mig = [t for t in rows if "django_migrations" in t]
print("migrations table(s):", mig)
con.close()

