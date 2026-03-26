import dlt

from pyspark.sql.functions import *

@dlt.view(
    name = "customers_gold_view"
)

#GOLD STREAMING VIEW ON TOP OF SLIVER VIEW (NOT ON SLIVER TABLE)

def customers_gold_view():
    df = spark.readStream.table("customers_sliver_view")
    return df


#CREATE DIM SCD TYPE-2 TABLE (WITH AUTO CDC)

dlt.create_streaming_table(name="dim_customers")


dlt.create_auto_cdc_flow(
    target = "dim_customers",
    source  = "customers_gold_view",
    keys = ["customer_id"],
    sequence_by = col("processed_date"),
    stored_as_scd_type=2,
    except_column_list = ["processed_date"]
)

