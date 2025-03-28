
# 🏆 595. Big Countries | Python Pandas Solution 🚀  

## **Intuition**  
The problem requires us to find "big countries" based on two conditions:  
- A country is considered **big** if its **area** is at least `3,000,000` square km.  
- OR its **population** is at least `25,000,000`.  

Since we are given a `DataFrame`, we need to filter out rows that satisfy either of these conditions and return only the required columns (`name`, `population`, `area`).  

## **Approach**  
1. **Filter** the `world` DataFrame using a boolean condition:  
   - `world['area'] >= 3000000` OR  
   - `world['population'] >= 25000000`  
2. **Select** only the relevant columns: `name`, `population`, `area`.  
3. **Return** the resulting DataFrame.  

### **Code**
```python
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filtering the big countries based on the given conditions
    big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Selecting required columns
    return big_countries_df[['name', 'population', 'area']]
```

## **Complexity Analysis**  
- **Time Complexity:** $$O(n)$$, where `n` is the number of rows in the DataFrame.  
  - We scan the DataFrame once to filter rows.  
- **Space Complexity:** $$O(1)$$ (excluding output storage).  
  - We are creating a filtered view of the DataFrame, not extra data structures.  

## **Example**  
### **Input:**  
```rb
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
```

### **Output:**  
```rb
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```
## 🎯 Feel free to ask any questions. 🚀