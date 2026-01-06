from influxdb import InfluxDBClient
import sys

P95_LIMIT_MS = 2000

client = InfluxDBClient(
    host="127.0.0.1",
    port=8086,
    database="jmeter"
)

query = """
SELECT last("pct95.0") AS p95
FROM jmeter
WHERE time > now() - 15m
"""

result = list(client.query(query).get_points())

if not result or result[0].get("p95") is None:
    print("No SLA data found in InfluxDB")
    sys.exit(1)

p95 = result[0]["p95"]
print(f"P95 Response Time = {p95} ms")

if p95 > P95_LIMIT_MS:
    print("SLA FAILED")
    sys.exit(1)

print("SLA PASSED")
sys.exit(0)
