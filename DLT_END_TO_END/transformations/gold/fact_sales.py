import dlt

from pyspark.sql.functions import *

@dlt.view(
    name = "sales_gold_view"
)

#GOLD STREAMING VIEW ON TOP OF SLIVER VIEW (NOT ON SLIVER TABLE)

def sales_gold_view():
    df = spark.readStream.table("sales_sliver_view")
    return df


#CREATE FACT TABLE ( WITH AUTO CDC)

dlt.create_streaming_table(name="fact_sales")


dlt.create_auto_cdc_flow(
    target = "fact_sales",
    source  = "sales_gold_view",
    keys = ["sales_id"],
    sequence_by = col("processDate"),
    stored_as_scd_type=1
)


