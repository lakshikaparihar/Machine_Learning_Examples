# World Development Indiacator


----
### Some Scala points

* ```val var_name = sqlContext.read.format("csv").option("header","true").option("inferSchema","true").load(file_path)``` : used to create the dataframe

* ```var_name.createOrReplaceTempView(temp_view_name)``` : used to create the temp view of the data for sql query 

