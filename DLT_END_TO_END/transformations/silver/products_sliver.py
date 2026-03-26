import dlt

from pyspark.sql.functions import *
#STREAMING VIEW
@dlt.view(
    name = "products_sliver_view"
)

def products_sliver_view():
    df_prod = spark.readStream.table("products_bronze")
    df_prod = df_prod.withColumn("processDate", current_timestamp())
    return df_prod

#PRODUCTS SILVER TABLE (WITH UPSERT)

dlt.create_streaming_table(name ="products_sliver")
dlt.create_auto_cdc_flow(
    target = "products_sliver",
    source  = "products_sliver_view",
    keys = ["product_id"],
    sequence_by = col("processDate"),
    stored_as_scd_type=1
)

