import dlt

from pyspark.sql.functions import *
#STREAMING VIEW
@dlt.view(
    name = "customers_sliver_view"
)

def customers_sliver_view():
    df_cust = spark.readStream.table("customers_bronze")
    df_cust = df_cust.withColumn("name",lower(col("name")))
    df_cust = df_cust.withColumn("Domain", split(col("email"), "@")[1])
    df_cust = df_cust.withColumn("processed_date", current_timestamp())
    return df_cust

#CUSTOMERS SILVER TABLE (WITH UPSERT)

dlt.create_streaming_table(name ="customers_sliver")


dlt.create_auto_cdc_flow(
    target = "customers_sliver",
    source  = "customers_sliver_view",
    keys = ["customer_id"],
    sequence_by = col("processed_date"),
    stored_as_scd_type=1
)

