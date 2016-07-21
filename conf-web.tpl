#!/bin/bash
### BEGIN INIT INFO
# Provides:          Arduino-OPC-UA
# Required-Start:    $syslog
# Required-Stop:     $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Arduino - OPC-UA server
# Description: Free implementation for web and OPC-UA access to one ore more arduino boards
#
### END INIT INFO

ADDRESS='0.0.0.0'
PYTHON="/opt/django/bin/python"
GUNICORN="gunicorn"
__PROJECTLOC__
MANAGELOC="arduino_ua_monitor.wsgi:application"
DEFAULT_ARGS="--workers=2 --daemon --log-file /var/log/webinterface.log   --bind=$ADDRESS:"
BASE_CMD="$GUNICORN $MANAGELOC $DEFAULT_ARGS"

SERVER1_PORT='8000'
SERVER1_PID="$PROJECTLOC/$SERVER1_PORT.pid"
start_server () {
  if [ -f $1 ]; then
    #pid exists, check if running
    if [ "$(ps -p `cat $1` | wc -l)" -gt 1 ]; then
       echo "Server already running on ${ADDRESS}:${2}"
       return
    fi
  fi
  __SOURCE2__ 
  cd $PROJECTLOC
  echo "starting ${ADDRESS}:${2}"
  echo $BASE_CMD$2
  $BASE_CMD$2 --pid=$1
}


stop_server (){
  if [ -f $1 ] && [ "$(ps -p `cat $1` | wc -l)" -gt 1 ]; then
    echo "stopping server ${ADDRESS}:${2}"
    kill -9 `cat $1`
    rm $1
  else
    if [ -f $1 ]; then
      echo "server ${ADDRESS}:${2} not running"
    else
      echo "No pid file found for server ${ADDRESS}:${2}"
    fi
  fi
}

case "$1" in
'start')
  start_server $SERVER1_PID $SERVER1_PORT
  ;;
'stop')
  stop_server $SERVER1_PID $SERVER1_PORT
  ;;
'restart')
  stop_server $SERVER1_PID $SERVER1_PORT
  sleep 12
  start_server $SERVER1_PID $SERVER1_PORT
  ;;
*)
  echo "Usage: $0 { start | stop | restart }"
  ;;
esac

exit 0
