# cg-penrose

## Running

0. Create virtualenv and install the requirements

    ```bash
    $ virtualenv -p python3 env  
    $ source env/bin/activate
    # Now install the requirements
    $ pip install -r requirements.txt
    ```

1. Compile the UI

    ```bash
    $ python setup.py build_ui
    ```
    
2. Install the package

    ```bash
    $ pip install -e .
    ```
    
3. Run the app

    ```bash
    $ python -m penrose
    ```

Computer Graphics Project [CMN08S1] - Allex Lima, Paulo Igor Moraes and Renan Barroncas
