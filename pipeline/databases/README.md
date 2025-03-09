## Relational vs Non-Relational Databases

### 1. What’s a Relational Database?
A **Relational Database** stores data in structured tables with rows and columns. Relationships between tables are established using foreign keys.
- **Examples:** MySQL, PostgreSQL, SQLite, SQL Server
- **Best for:** Structured, transactional data (e.g., banking, healthcare, e-commerce)

### 2. What’s a Non-Relational Database?
A **Non-Relational Database (NoSQL)** does not use tables. Instead, it stores data in formats like documents, key-value pairs, wide-column stores, or graphs.
- **Examples:** MongoDB, Cassandra, Redis, Neo4j
- **Best for:** Big data, flexible schemas, high scalability

### 3. Difference Between SQL and NoSQL

| Feature            | SQL (Relational) | NoSQL (Non-Relational) |
|--------------------|----------------|-----------------------|
| **Structure**      | Tables (Rows & Columns) | Documents, Key-Value, Graph, Column-Family |
| **Schema**        | Fixed Schema (Predefined) | Dynamic Schema (Flexible) |
| **Scalability**   | Vertical Scaling | Horizontal Scaling |
| **Transactions**  | Strong ACID Compliance | BASE (Eventual Consistency) |
| **Best For**      | Structured, transactional data | Big data, real-time applications |

---

## SQL Database Operations

### 4. Creating Tables with Constraints
```sql
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Age INT CHECK (Age > 0),
    Gender VARCHAR(10) CHECK (Gender IN ('Male', 'Female'))
);
```

### 5. Optimizing Queries with Indexes
```sql
CREATE INDEX idx_patient_name ON Patients(Name);
```

### 6. Stored Procedures in MySQL
```sql
DELIMITER //
CREATE PROCEDURE GetMalePatients()
BEGIN
    SELECT * FROM Patients WHERE Gender = 'Male';
END //
DELIMITER ;
```
```sql
CALL GetMalePatients();
```

### 7. Views in MySQL
```sql
CREATE VIEW ActivePatients AS
SELECT PatientID, Name, Age FROM Patients WHERE Status = 'Active';
```

### 8. Triggers in MySQL
```sql
CREATE TABLE DeletedPatientsLog (
    LogID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    DeletedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER AfterPatientDelete
AFTER DELETE ON Patients
FOR EACH ROW
BEGIN
    INSERT INTO DeletedPatientsLog (PatientID) VALUES (OLD.PatientID);
END //
DELIMITER ;
```

---

## Database Concepts

### 9. ACID Properties
- **Atomicity** → All operations in a transaction succeed or fail together.
- **Consistency** → Database remains in a valid state.
- **Isolation** → Transactions do not interfere with each other.
- **Durability** → Data is permanently saved after a transaction.

### 10. Document Storage (NoSQL)
Example MongoDB document:
```json
{
    "PatientID": 1,
    "Name": "John Doe",
    "Age": 45,
    "Diagnosis": "Liver Disease"
}
```

### 11. NoSQL Types
1. **Document Stores** (MongoDB) → JSON-based documents.
2. **Key-Value Stores** (Redis) → Simple key-value pairs.
3. **Wide-Column Stores** (Cassandra) → Columns grouped into families.
4. **Graph Databases** (Neo4j) → Nodes & relationships.

### 12. Benefits of NoSQL
✅ Schema Flexibility  
✅ High Scalability  
✅ Better for Big Data  
✅ Faster Queries

---

## MongoDB Operations

### 13. Querying Data in MongoDB
```js
db.Patients.find();
db.Patients.find({ Age: { $gt: 40 } });
db.Patients.findOne({ Name: "John Doe" });
```

### 14. Inserting, Updating, and Deleting Data
```js
db.Patients.insertOne({ Name: "John Doe", Age: 45, Gender: "Male", Diagnosis: "Liver Disease" });
db.Patients.updateOne({ Name: "John Doe" }, { $set: { Age: 50 } });
db.Patients.deleteOne({ Name: "John Doe" });
```

### 15. Using MongoDB
```sh
mongod --dbpath /data/db  # Start MongoDB
mongo  # Open Mongo Shell
use HospitalDB;  # Create/Use Database
db.createCollection("Patients");  # Create Collection
db.Patients.insertOne({ Name: "Jane Doe", Age: 30 });
db.Patients.find();