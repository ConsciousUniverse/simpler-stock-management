# Simpler Stock Management (Beta)

Simpler Stock Management is a web application designed to help manage warehouse and shop stock efficiently. The application provides features for searching, sorting, updating, and transferring stock items between the warehouse and shops. Data is stored in a local SQLite3 database.

## Features

### User Authentication
- **Login/Logout**: Users can log in and log out of the application.
- **User Status**: Displays the logged-in user's status.

### Stock Management
- **Warehouse Stock**: View and manage items in the warehouse.
- **Shop Stock**: View items available in the shop.
- **Transfers Pending**: View and manage pending stock transfers.

### Search and Sort
- **Search**: Search for items in the warehouse and shop by SKU, description, or other attributes.
- **Sort**: Sort items by SKU, description, retail price, or quantity.

### Update Mode
- **Toggle Update Mode**: Managers can enter and leave update mode to make changes to item details.
- **Update Items**: Managers can update item descriptions, retail prices, and quantities.
- **Delete Items**: Managers can delete items from the warehouse stock.

### Transfer Items
- **Transfer Items**: Shop users can request to transfer items from the warehouse to the shop.
- **Complete Transfers**: Managers can dispatch or cancel pending transfers from the warehouse to the shops. Warehouse inventory is only reduced - and shop inventory increased - after managers have actioned the dispatch on the system.

## License

Simpler Stock Management is licensed under the GPLv3. See the [LICENSE](LICENSE) file for more details.

## Author

Dan Bright - [GitHub](https://github.com/consciousuniverse), github@bright.contact