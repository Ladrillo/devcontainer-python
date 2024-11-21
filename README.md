# Python3 DevContainer

1. Create an `.env` file and place it inside the `.devcontainer` folder.

    ```text
    OPENAI_API_KEY=abcd
    ```

    This is an example. Replace `abcd` with desired value.

2. Reopen the project in a dev container.

3. Install new dependencies in your project if needed:

    ```bash
    pip install openai && pip freeze > requirements.txt
    ```

4. Have fun!

    ```bash
    pip list
    pip list --outdated
    pip list --not-required
    python main.py
    ```
