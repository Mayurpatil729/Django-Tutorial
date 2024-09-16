<!-- @format -->

## Django Admin Panel Setup and Usage

### 1. Running Initial Migrations

Before using the Django admin panel, you need to run the migrations to create the necessary database tables.

```bash
python manage.py migrate
```

This command applies migrations, including the built-in migrations for Django’s authentication and admin system, which are required for the admin panel to work.

### 2. Creating a Superuser

The **superuser** has full access to the admin panel. To create a superuser, run the following command:

```bash
python manage.py createsuperuser
```

You’ll be prompted to enter the following details:

- **Username**: Choose a username for the superuser.
- **Email Address**: Provide a valid email.
- **Password**: Enter and confirm a strong password.

### 3. Accessing the Admin Panel

1. **Run the Django Development Server**:

   Start the Django server by running:

   ```bash
   python manage.py runserver
   ```

2. **Access the Admin Panel**:

   Open your web browser and go to the following URL:

   ```
   http://localhost:8000/admin/
   ```

   You’ll be prompted to log in using the credentials of the superuser you created.

### 4. Registering Models in Admin

By default, the Django admin panel only manages a few built-in models such as `User` and `Group`. To manage your own app’s models in the admin interface, you need to register them.

In your app’s `admin.py` file, register the models you want to manage through the admin panel.

#### Example: Registering a Model

In your app’s `admin.py`, register your model like this:

```python
from django.contrib import admin
from .models import MyModel  # Import your model

# Register your model
admin.site.register(MyModel)
```

After registering, your model will appear in the Django admin interface.

### 5. Customizing the Admin Panel

You can customize how the models appear and behave in the admin panel by using the `ModelAdmin` class.

#### Example: Customizing a Model’s Admin View

```python
from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')  # Fields to display in the list view
    search_fields = ('name',)  # Fields you can search by
    list_filter = ('is_active', 'created_at')  # Filters in the sidebar

admin.site.register(MyModel, MyModelAdmin)
```

- **`list_display`**: Controls which fields are shown in the list view.
- **`search_fields`**: Adds a search bar to search by specific fields.
- **`list_filter`**: Adds filters in the sidebar for easy filtering.

### 6. Admin Panel Commands

Here’s a list of essential commands for working with Django’s admin panel:

1. **Run Migrations**:
   Apply migrations to prepare the database (including admin models):

   ```bash
   python manage.py migrate
   ```

2. **Create Superuser**:
   Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Server**:
   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

4. **Change User Password**:
   If you forget your superuser password, you can reset it via the command line:

   ```bash
   python manage.py changepassword <username>
   ```

   Example:

   ```bash
   python manage.py changepassword admin
   ```

5. **Shell Access**:
   Use the Django shell to interact with the database directly, including creating or updating users:

   ```bash
   python manage.py shell
   ```

   Example of creating a user in the shell:

   ```python
   from django.contrib.auth.models import User
   user = User.objects.create_user('john', 'john@example.com', 'password123')
   user.is_superuser = True
   user.is_staff = True
   user.save()
   ```

---

### 7. Additional Admin Customization

You can further customize the Django admin panel in several ways:

- **Adding Inline Models**: Manage related models in the same form as the parent model.

  Example:

  ```python
  from django.contrib import admin
  from .models import Author, Book

  class BookInline(admin.TabularInline):
      model = Book

  class AuthorAdmin(admin.ModelAdmin):
      inlines = [BookInline]

  admin.site.register(Author, AuthorAdmin)
  ```

- **Customizing Admin Actions**: Add custom actions to perform on multiple objects in the admin panel.

  Example:

  ```python
  def make_active(modeladmin, request, queryset):
      queryset.update(is_active=True)

  make_active.short_description = "Mark selected items as active"

  class MyModelAdmin(admin.ModelAdmin):
      actions = [make_active]

  admin.site.register(MyModel, MyModelAdmin)
  ```

### 8. Logout from the Admin Panel

To log out from the admin panel, simply go to:

```
http://localhost:8000/admin/logout/
```

This will log you out of the Django admin interface.

---

By following these steps, you’ll be able to set up and manage your Django admin panel, register models, and customize the admin interface for a better experience.
