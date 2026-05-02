# export PYTHONPATH=$(dirname $(dirname "$(realpath $0)"))/src
# TODO: Remove the above line, we don't need this anymore.
python3 -m unittest discover tests/ "$@" -v