set -x

pip3 install -r /requirements.txt

if [ $DEBUG -eq 1 ]
then
   /usr/bin/tail -f /dev/null
fi
uvicorn main:app --host 0.0.0.0 --port 8000 # TODO Verify