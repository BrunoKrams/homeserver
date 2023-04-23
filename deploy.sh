TARGET_DIRECTORY="/home/markus/homeserver"

PID=$(ssh markus@homeserver ps -aux | grep "[p]ython3 -m main.app_prod_pi" | awk '{print $2}')
while ssh markus@homeserver "kill $PID" 2>/dev/null; do
    sleep 1
done

ssh markus@homeserver "rm -rf $TARGET_DIRECTORY"

rsync -r /home/markus/workspace/homeserver/main markus@homeserver:$TARGET_DIRECTORY

#ssh markus@homeserver "cd $TARGET_DIRECTORY && nohup python3 -m main.app_prod_pi &"
