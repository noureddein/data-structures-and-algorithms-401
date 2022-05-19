# Hashtables

## Summary
<!-- Short summary or background information -->
- Hashing is a technique or process of mapping keys/values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.
- Hash tables are a data structure that utilizes key/value pairs. This means every Node or Bucket has both a key and a value.


## Challenge
<!-- Description of the challenge -->
  - ### Implement a Hashtable Class with the following methods:

    - set
      - Arguments: key, value
      - Returns: nothing
      - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
      - Should a given key already exist, replace its value from the value argument given to this method.
    - get
      - Arguments: key
      - Returns: Value associated with that key in the table
    - contains
      - Arguments: key
      - Returns: Boolean, indicating if the key exists in the table already.
    - keys
      - Returns: Collection of keys
    - hash
      - Arguments: key
      - Returns: Index in the collection for that key

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
  - **Approach**:
    - The approach here is creating a class that contain all methods.
    - Each input validated using a function.
  - **Efficiency**
    - Time complexity O(n).
    - Space complexity O(n).

## API
<!-- Description of each method publicly available in each of your hashtable -->
  - Methods
    1. Set(): Used to insert data in the hash table, the method take key and value arguments.
    2. Get(): Used to retrieve a value depending on the passed key.
    3. Contains(): Check if a a key exist or not and return a boolean.
    4. Keys(): Used to retrieve all available keys in the hash table.