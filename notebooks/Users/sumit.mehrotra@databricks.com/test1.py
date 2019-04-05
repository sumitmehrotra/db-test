# Databricks notebook source
# MAGIC %fs head /databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE temp_diamonds_sumit
# MAGIC   USING csv
# MAGIC   OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header "true", mode "FAILFAST")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from temp_diamonds_sumit
# MAGIC --remark