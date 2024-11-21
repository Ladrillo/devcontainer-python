# Python3 DevContainer

1. Create an `.env` file and place it inside the `.devcontainer` folder.

    ```text
    OPENAI_API_KEY=abcd
    ```

    This is an example. Replace `abcd` with desired values.

2. Reopen the project in a dev container.

3. Install dependencies for your project:

    ```bash
    pip install openai
    ```

4. Update your requirements.txt file:

    ```bash
    pip freeze > requirements.txt
    ```

5. Have fun!
