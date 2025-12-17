# The CRUD Maker Template 🍽️

A template for Python CRUD applications based on Clean Architecture.

### Introduction and Objectives ⁉

The main objective is to provide a template for creating robust and maintainable CRUD (Create, Read, Update, Delete) applications. This architecture is based on the principles of Clean Architecture, promoting separation of concerns and scalability.

### Clean Architecture 🧼🏰

The purpose of the project is to implement a Clean Architecture for stateless microservices. This approach structures the code in layers, each with a specific responsibility, based on SOLID principles. It helps in creating testable, maintainable, and independent components.

### Folder Structure 🌳

The folder structure is organized to support the Clean Architecture principles, with a clear separation between modules and shared code.

```
.
|____tests
| |____shared
| | |____infra
| | | |____dto
| | | |____repositories
| | |____domain
| | | |____entities
| | |____helpers
| |____modules
| | |____create_user
| | | |____app
| | |____update_user
| | | |____app
| | |____get_all_users
| | | |____app
| | |____delete_user
| | | |____app
| | |____get_user
| | | |____app
|____docs
|____src
| |____shared
| | |____infra
| | | |____dto
| | | |____repositories
| | | | |____mock
| | | | |____dynamo
| | | | |____mongodb
| | | |____external
| | | | |____dynamo
| | | | | |____datasources
| | |____decorators
| | |____domain
| | | |____enums
| | | |____repositories
| | | |____observability
| | | |____entities
| | |____helpers
| | | |____enum
| | | |____functions
| | | |____errors
| | | |____external_interfaces
| |____modules
| | |____create_user
| | | |____app
| | |____update_user
| | | |____app
| | |____get_all_users
| | | |____app
| | |____delete_user
| | | |____app
| | |____get_user
| | | |____app
```

## Naming Conventions 📛

### Files and Directories 📁

-   Files are named after the classes they contain.
-   Use **snake_case** (e.g., `create_user_controller.py`).

### Classes 🕴️

-   Use **CamelCase** (e.g., `CreateUserController`).
-   **Interfaces**: Start with `I` (e.g., `IUserRepository`).
-   **Repository**: Same name as the interface without the `I`, and with the implementation type as a suffix (e.g., `UserRepositoryMock`, `UserRepositoryMongo`).
-   **Controller**: Ends with `Controller` (e.g., `CreateUserController`).
-   **Usecase**: Ends with `Usecase` (e.g., `CreateUserUsecase`).
-   **Viewmodel**: Ends with `Viewmodel` (e.g., `CreateUserViewmodel`).
-   **Presenter**: Ends with `Presenter` (e.g., `CreateUserPresenter`).

### Methods 👨‍🏫

-   Use **snake_case**.
-   Prefer verb-based names (e.g., `create_user`, `get_user`).

### Variables 🅰️

-   Use **snake_case**.
-   Avoid using verbs.

### Enums

-   Enum members use **SNAKE_CASE**.
-   File names use **snake_case** (e.g., `state_enum.py`).

### Tests 📄

-   Use **snake_case**.
-   File names must start with `test_` for pytest to discover them (e.g., `test_create_user_usecase.py`).

## Installation 👩‍💻

1.  **Clone the repository**

2.  **Create a virtual environment**

    ```bash
    # For Windows
    python -m venv venv

    # For Linux/macOS
    python3 -m venv venv
    ```

3.  **Activate the virtual environment**

    ```bash
    # For Windows
    .\venv\Scripts\activate

    # For Linux/macOS
    source venv/bin/activate
    ```

4.  **Install the requirements**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project 🚀

The application uses an environment variable `ENV` to determine which repository implementation to use.

-   **local**: Uses mock repositories for development and testing.
-   **dev, hml, prd**: Uses a MongoDB repository.

### To run locally:

1.  Set the environment variable.

    ```bash
    # For Windows (PowerShell)
    $env:ENV="local"

    # For Linux/macOS
    export ENV=local
    ```

2.  Run the Flask application.

    ```bash
    functions-framework --target=my_crud
    ```
    The application will be available at `http://127.0.0.1:8080`.

### To run the tests:

```bash
pytest
```

## Special Thanks and References 🙏

- [Clean MSS Template (Dev. Community Mauá)](https://github.com/Maua-Dev/clean_mss_template)
- [Dev. Community Mauá](https://www.instagram.com/devcommunitymaua/)
- [Clean Architecture: A Craftsman's Guide to Software Structure and Design](https://www.amazon.com.br/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)