## How to Handle missing values ?
1. **Using Median**<br>

    * Find the median of the column which contains NaN values , Example : <br>
      
        ```
        df.experiences.median()
        ```

    * Convert the median to the integer value <br>
       ```
       math.floor(df.experiences.median())
       ```

    * replace the NaN value with the median
       ```
       df.experience.fillna(math.floor(df.experiences.median()))
        ```



---------------


## How to convert the numbers in word form with their integer form
<br>

**Example:** <br>
* Zero --> 0 
* five --> 5 

<br>

>pip install word2number

<br>

```
   from word2number import w2n
   df.experience.apply(w2n.word_to_num)
```
