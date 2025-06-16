import streamlit as st
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "TSP 2 MINI PROJECT"
org = "NA"
token = "JL_Xx3ZCyXyl71EG_q902tRcHkFqZpeNiFBiqCVfzwChiAVLw_gTQ_NnK3qLOfHkn-44e9CmXRaSDBoi-mSZsQ=="

url ="http://localhost:8086"

client = influxdb_client.InfluxDBClient(
   url = url,
   token = token,
   org = org,
   bucket = bucket
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("_measurement").tag("location", "Prague").field("L1_V", 11.5)
write_api.write(bucket=bucket, org=org, record=p)

query_api = client.query_api()
query = 'from(bucket:"TSP 2 MINI PROJECT")\
|> range(start: -1h)\
|> filter(fn:(r) => r._measurement == "TNB_1")\
|> filter(fn:(r) => r._field == "L1_V")'
result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

st.print(results)
