#! /bin/bash -e

sudo ./kill_server.sh
echo "Starting up Dojo Docs..."
python /projects/dojo-docs/app/app.py &> /dev/null
chmod 666 /tmp/docs.sock
# gunicorn -w 4 --worker-class="egg:meinheld#gunicorn_worker" -b unix:/tmp/docs.sock -m 005 api:app --daemon &> /dev/null
