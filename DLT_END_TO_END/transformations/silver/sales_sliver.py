import dlt

from pyspark.sql.functions import *
#STREAMING VIEW
@dlt.view(
    name = "sales_sliver_view"
)

def sales_sliver_view():
    df_sales = spark.readStream.table("sales_bronze")
    df_sales = df_sales.withColumn("priceforsale", round(col("totaL_amount")/col("quantity"),2))
    df_sales = df_sales.withColumn("processDate", current_timestamp())
    return df_sales

#SALES SILVER TABLE (WITH UPSERT)

dlt.create_streaming_table(name ="sales_sliver")
dlt.create_auto_cdc_flow(
    target = "sales_sliver",
    source  = "sales_sliver_view",
    keys = ["sales_id"],
    sequence_by = col("processDate"),
    stored_as_scd_type=1
)

