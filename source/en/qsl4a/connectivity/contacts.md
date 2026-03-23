# Contacts API

Access and manage device contacts.

## Contact Picking

### pickContact()
Display a list of contacts to pick from.

```python
pickContact()
```

**Returns:** Intent with contact URI

### pickPhone()
Display a list of phone numbers to pick from.

```python
pickPhone()
```

**Returns:** Selected phone number string

## Contact Queries

### contactsGet()
Get all contacts.

```python
contactsGet(attributes=None)
```

**Parameters:**
- `attributes` (list, optional): Specific attributes to retrieve

**Returns:** List of contact JSONObject

### contactsGetById()
Get a contact by ID.

```python
contactsGetById(id, attributes=None)
```

**Parameters:**
- `id` (int): Contact ID
- `attributes` (list, optional): Specific attributes to retrieve

**Returns:** JSONObject contact data

### contactsGetCount()
Get the total number of contacts.

```python
contactsGetCount()
```

**Returns:** Integer count

### contactsGetIds()
Get all contact IDs.

```python
contactsGetIds()
```

**Returns:** List of contact ID integers

### contactsGetAttributes()
Get all possible contact attributes.

```python
contactsGetAttributes()
```

**Returns:** List of attribute names

## Content Queries

### queryContent()
Query content resolver with custom parameters.

```python
queryContent(uri, attributes=None, selection=None, selectionArgs=None, order=None)
```

**Parameters:**
- `uri` (str): Content URI
- `attributes` (list, optional): Attributes to retrieve
- `selection` (str, optional): WHERE clause
- `selectionArgs` (list, optional): Selection arguments
- `order` (str, optional): ORDER BY clause

**Returns:** List of JSONObject results

### queryAttributes()
Get attributes for a content URI.

```python
queryAttributes(uri)
```

**Parameters:**
- `uri` (str): Content URI

**Returns:** JSONArray of attribute names

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Pick a contact
contact_uri = droid.pickContact().result
print(f"Selected contact: {contact_uri}")

# Pick a phone number
phone = droid.pickPhone().result
print(f"Selected phone: {phone}")

# Get all contacts
contacts = droid.contactsGet().result
print(f"Total contacts: {len(contacts)}")

# Get contact by ID
contact = droid.contactsGetById(1).result
print(f"Contact: {contact}")

# Get contact attributes
attrs = droid.contactsGetAttributes().result
print(f"Available attributes: {attrs}")
```
