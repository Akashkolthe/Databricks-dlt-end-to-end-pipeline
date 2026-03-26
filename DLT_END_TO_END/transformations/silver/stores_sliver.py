import dlt

from pyspark.sql.functions import *
#STREAMING VIEW
@dlt.view(
    name = "stores_sliver_view"
)

def stores_sliver_view():
    df_str = spark.readStream.table("stores_bronze")
    df_str = df_str.withColumn("store_name",regexp_replace(col("store_name"),"_",""))
    df_str = df_str.withColumn("processDate", current_timestamp())
    return df_str

#STORES SILVER TABLE (WITH UPSERT)

dlt.create_streaming_table(name ="stores_sliver")

dlt.create_auto_cdc_flow(
    target = "stores_sliver",
    source  = "stores_sliver_view",
    keys = ["store_id"],
    sequence_by = col("processDate"),
    stored_as_scd_type=1
)

