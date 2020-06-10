poetry run pytest -v --cov=fortytwocli --cov-report=html 
if [ "$(uname)" == "Darwin" ]; then
    open ./htmlcov/index.html
elif [ "$(expr substr $(uname -s) 1 5)" == "MINGW" ]; then
    start ./htmlcov/index.html
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    xdg-open ./htmlcov/index.html
else
    echo "please check 'fortytwocli/htmlcov/index.html'."
fi
