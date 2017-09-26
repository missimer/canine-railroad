.PHONY: tests run clean

SOURCE_VENV:=source venv/bin/activate &&

run: venv
	$(SOURCE_VENV) python src/app.py

tests: venv
	$(SOURCE_VENV) nose2 -c unittest.cfg
	$(SOURCE_VENV) coverage report > /dev/null

venv: requirements.txt
	rm -rf venv
	virtualenv --python=python3.5 venv
	./venv/bin/pip install -r requirements.txt

clean:
	find -name "*~" -delete
	rm -rf venv
