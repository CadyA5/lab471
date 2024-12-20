# Lab 10

## Overview

- **Student** model with a ForeignKey to **Address**.
- **CRUD operations** for adding, viewing, editing, and deleting students and addresses.
- Templates and forms for managing students and their associated addresses.

## Features

1. **Models**:
   - **Student**: Includes fields for `name`, `age`, and a ForeignKey to **Address**.
   - **Address**: Includes a `city` field to store the student's address.

2. **Views**:
   - **List Students**: Displays all students and their associated addresses.
   - **Add Student**: Form to add a new student and their address.
   - **Edit Student**: Form to update an existing student's details and address.
   - **Delete Student**: Deletes a student from the database.
   - **Add Address**: Adds a new address to the database.

3. **Forms**:
   - Forms for **Student** and **Address** creation and updates.

4. **URLs**:
   - Routes for all CRUD operations (`list`, `add`, `edit`, `delete`).

