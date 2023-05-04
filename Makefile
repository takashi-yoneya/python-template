# .PHONYで定義することで、タスクランナーを簡単に定義できます

# install
.PHONY: install
install:
	pyenv install 3.10
	poetry env use 3.10
	poetry install
	pre-commit install

# main.pyを実行する
.PHONY: run_main
run_main:
	python src/main.py

# pre-commitを明示的に実行する
.PHONY: pre-commit
pre-commit:
	poetry run pre-commit run --all-files

.PHONY: test
test:
	poetry run pytest tests
