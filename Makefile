ifeq ($(OS),Windows_NT)
# N/A
else
    all:
		virtualenv -p python3 env
		(source env/bin/activate; pip install -r requirements.txt; python setup.py build_ui; pip install -e .; deactivate;)
    install:
		ln -s penrose/__main__.py temp_bin.py
		(source env/bin/activate; pyinstaller --onefile --distpath bin -p ./env/lib/ temp_bin.py -n penrose; deactivate;)
		rm temp_bin.py
		rm -rf build/

    run:
		(source env/bin/activate; python -m penrose; deactivate;)

    clean:
		rm -rf build/ dist/ *.spec *.pyc  __pycache__/ *.egg-info
endif

