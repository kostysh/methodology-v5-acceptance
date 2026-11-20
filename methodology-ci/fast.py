"""Approved synthetic fast contract. Accept a unique positive ID and integer cents."""
import csv
import sys

reader = csv.DictReader(sys.stdin)
assert reader.fieldnames == ["id", "price_cents"]
ids = set()
for row in reader:
    product_id = int(row["id"])
    assert product_id > 0 and product_id not in ids
    assert int(row["price_cents"]) >= 0
    ids.add(product_id)
assert ids
