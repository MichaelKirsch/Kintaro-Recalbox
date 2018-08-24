#! /bin/sh
 
case "$1" in
  start)
    echo "Starting SNES"
    # run application you want to start
    python /opt/Kintaro/kintaro.py &
    ;;
  stop)
    echo "Stopping SNES"
    # kill application you want to stop
    killall python
    ;;
  *)
    echo "Usage: /etc/init.d/example{start|stop}"
    exit 1
    ;;
esac
 
exit 0
