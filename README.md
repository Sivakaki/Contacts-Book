# Contact Book Application

A simple and efficient command-line contact management system that allows users to store, view, search, and manage their contacts with ease.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [File Format](#file-format)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Add Contacts**: Store contact information including name, phone number, and email
- **View All Contacts**: Display all saved contacts in a formatted table
- **Search Contacts**: Find contacts by name with case-insensitive search
- **Delete Contacts**: Remove contacts from your contact book
- **Persistent Storage**: All contacts are saved in a CSV file for future access
- **User-Friendly CLI**: Interactive menu-driven interface

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses built-in Python libraries only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/contact-book.git
cd contact-book
```

2. Ensure Python is installed on your system:
```bash
python --version
```

3. Run the application:
```bash
python contacts_book.py
```

## Usage

Execute the program and follow the interactive menu:
```bash
python contacts_book.py
```

### Menu Options
--- Contact Book Menu ---

Add Contact
View Contacts
Search Contact
Delete Contact
Exit


Simply enter the number corresponding to your desired action and follow the prompts.

## Functions

### add_contact()
Adds a new contact to the contact book.

**User Input Required:**
- Name
- Phone Number
- Email

**Output:** Confirmation message upon successful storage

### view_contacts()
Displays all contacts stored in the contact book.

**Output:** Formatted list of all contacts with name, phone, and email

**Error Handling:** Notifies if no contacts exist or file is missing

### search_contact()
Searches for a contact by name.

**User Input Required:**
- Contact name to search

**Features:**
- Case-insensitive search
- Partial or exact name matching

**Output:** Contact details if found, or not found message

### delete_contact()
Deletes a contact from the contact book.

**User Input Required:**
- Name of contact to delete

**Output:** Confirmation of deletion or not found message

### main()
Entry point that runs the interactive menu loop.

## File Format

Contacts are stored in `contacts.txt` in CSV format:
name,phone,email
John Doe,1234567890,john@example.com
Jane Smith,9876543210,jane@example.com

## Examples

### Adding a Contact
Enter your choice: 1
Enter Name: John Doe
Enter Phone Number: 9876543210
Enter Email: john.doe@example.com
Contact saved successfully.

### Viewing Contacts
Enter your choice: 2
--- All Contacts ---
Name: John Doe | Phone: 9876543210 | Email: john.doe@example.com
Name: Jane Smith | Phone: 8765432109 | Email: jane.smith@example.com

### Searching a Contact
Enter your choice: 3
Enter name to search: john
Found -> Name: John Doe | Phone: 9876543210 | Email: john.doe@example.com

### Deleting a Contact
Enter your choice: 4
Enter name to delete: john
Contact successfully deleted!

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please ensure your code follows PEP 8 standards and includes appropriate comments.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

K Siva Rama Krishna

## Support

For issues or questions, please create an issue on GitHub or contact [sivakaki033@gmail.com].

---
